"""
Scenario Archive (zip) <-> internal ScenarioSerializer shape.

Per OVS Scenario Specification v1.11 SS2.2-2.5, a Scenario Archive is a zip
containing exactly one XML manifest (expected to be named 'main.xml', but a
differently-named file is tolerated per spec) plus three directories --
images/, vocals/, media/ -- holding the binary files the manifest references
by basename.

`OvsXMLParser` (app/parsers.py) works fine on well-formed subtrees, but two
real-world shapes break its generic "same tag => list" / "different tag =>
dict" inference:

  * <scene> elements are unwrapped siblings directly under <scenario> (the
    renderer's `flatten_keys` omits the <scenes> wrapper), so a plain dict
    conversion keeps only the last one.
  * <controls> mixes a single <color> with N <control> children, so its
    first child's tag ('color') is never in `list_item_tags`, and the whole
    element takes the dict branch, again keeping only the last <control>.

Both were confirmed against real scenario files (main-sepsis.xml has 8
<scene> siblings and 16 <control> children under one scene/profile), so this
module parses those two shapes explicitly instead of delegating to
`OvsXMLParser` for the whole document.
"""
import os
import zipfile
from xml.etree import ElementTree as ET

from app.parsers import OvsXMLParser

REQUIRED_DIRS = ('images', 'vocals', 'media')


class ScenarioArchiveError(Exception):
    """Raised for malformed archives or manifests referencing missing files."""

    def __init__(self, message, missing_files=None):
        super().__init__(message)
        self.missing_files = missing_files or []


def read_archive(file_obj):
    """Unpack an uploaded zip into (manifest_root, files).

    `files` is {'images': {basename: bytes}, 'vocals': {...}, 'media': {...}},
    always containing all three keys (empty dicts for directories absent from
    the zip -- the spec only requires the directories exist on import, not
    that the uploaded zip prove it packed them).
    """
    try:
        zf = zipfile.ZipFile(file_obj)
    except zipfile.BadZipFile as exc:
        raise ScenarioArchiveError('Uploaded file is not a valid zip archive') from exc

    with zf:
        names = [n for n in zf.namelist() if not n.endswith('/')]
        xml_names = [n for n in names if n.lower().endswith('.xml')]
        if len(xml_names) != 1:
            raise ScenarioArchiveError(
                'Scenario archive must contain exactly one XML file, found %d' % len(xml_names)
            )

        try:
            root = ET.fromstring(zf.read(xml_names[0]))
        except ET.ParseError as exc:
            raise ScenarioArchiveError('Could not parse manifest XML: %s' % exc) from exc

        files = {d: {} for d in REQUIRED_DIRS}
        for name in names:
            if name in xml_names:
                continue
            parts = name.split('/')[:-1]
            for d in REQUIRED_DIRS:
                if d in parts:
                    files[d][os.path.basename(name)] = zf.read(name)
                    break

    return root, files


def _convert(element):
    if element is None:
        return None
    return OvsXMLParser()._xml_convert(element)


def _controls_from_element(controls_el):
    if controls_el is None:
        return '#000000', []
    color_el = controls_el.find('color')
    color = color_el.text if color_el is not None and color_el.text else '#000000'
    controls = [_convert(c) for c in controls_el.findall('control')]
    return color, controls


def _clean_init(init_value):
    """Some real archives leave <init>, or individual <cardiac>/<respiration>/
    <general> sections within it, as empty/whitespace-only placeholders when
    there's no state override -- those convert to a bare string rather than a
    dict. Drop them so the (all-optional) init sub-serializers just treat the
    section as omitted instead of receiving invalid data."""
    if not isinstance(init_value, dict):
        return None
    cleaned = dict(init_value)
    for section in ('cardiac', 'respiration', 'general'):
        if section in cleaned and not isinstance(cleaned[section], dict):
            cleaned.pop(section)
    return cleaned


def _convert_scene(scene_el):
    scene = _convert(scene_el)
    if 'init' in scene:
        init = _clean_init(scene['init'])
        if init:
            scene['init'] = init
        else:
            scene.pop('init', None)
    return scene


def _eventgroups_from_element(events_el):
    """<category> mixes <name>/<title> with repeated <event> children, the
    same shape that breaks <controls> above -- same manual fix needed."""
    if events_el is None:
        return []
    eventgroups = []
    for category_el in events_el.findall('category'):
        eventgroups.append({
            'name': category_el.findtext('name') or '',
            'title': category_el.findtext('title') or '',
            'events': [_convert(e) for e in category_el.findall('event')],
        })
    return eventgroups


def manifest_to_internal(root):
    """Reshape a parsed <scenario> manifest into two pieces:

    - `scenario_payload`: ready for `ScenarioSerializer(data=...)`. Vocal/media
      file lists are emptied and avatar/summary filenames stripped here --
      actual file bytes are attached afterward via the same per-file
      endpoints the wizard uses (app/views.py ScenarioVocals/Media/Images),
      not through the main nested serializer (see ADR-0002: nested writes
      don't carry file bytes over multipart reliably).
    - `file_refs`: the filenames/titles needed to perform that attachment,
      plus every filename referenced so callers can validate the archive
      actually contains them before creating any DB rows.
    """
    profile_el = root.find('profile')
    color, controls = _controls_from_element(
        profile_el.find('controls') if profile_el is not None else None
    )

    profile = _convert(profile_el) or {}
    profile['color'] = color
    profile['controls'] = controls

    avatar_filename = None
    if profile.get('avatar'):
        avatar_filename = profile['avatar'].pop('filename', None)
    summary_image = None
    if profile.get('summary'):
        summary_image = profile['summary'].pop('image', None)

    vocals_el = root.find('vocals')
    media_el = root.find('media')

    # Some real archives use an empty placeholder (e.g. `<file><!-- None --></file>`)
    # for an intentionally-empty <vocals>/<media> list -- filter out anything
    # that isn't a proper {filename, title} entry.
    vocalfiles = [f for f in (_convert(vocals_el) or []) if isinstance(f, dict) and f.get('filename')] \
        if vocals_el is not None else []
    mediafiles = [f for f in (_convert(media_el) or []) if isinstance(f, dict) and f.get('filename')] \
        if media_el is not None else []

    scenario_payload = {
        'header': _convert(root.find('header')),
        'profile': profile,
        'vocalfiles': [],
        'mediafiles': [],
        'init': _convert(root.find('init')),
        'eventgroups': _eventgroups_from_element(root.find('events')),
        'scenes': [_convert_scene(scene_el) for scene_el in root.findall('scene')],
    }

    file_refs = {
        'avatar': avatar_filename,
        'summary': summary_image,
        'vocals': vocalfiles,   # [{'filename':, 'title':}, ...]
        'media': mediafiles,    # [{'filename':, 'title':}, ...]
    }

    return scenario_payload, file_refs


def missing_referenced_files(file_refs, files):
    """Return {'images': [...], 'vocals': [...], 'media': [...]} of filenames
    referenced by the manifest but not present in the archive's directories."""
    missing = {'images': [], 'vocals': [], 'media': []}

    if file_refs['avatar'] and file_refs['avatar'] not in files['images']:
        missing['images'].append(file_refs['avatar'])
    if file_refs['summary'] and file_refs['summary'] not in files['images']:
        missing['images'].append(file_refs['summary'])
    for vocal in file_refs['vocals']:
        if vocal.get('filename') not in files['vocals']:
            missing['vocals'].append(vocal.get('filename'))
    for media in file_refs['media']:
        if media.get('filename') not in files['media']:
            missing['media'].append(media.get('filename'))

    return {k: v for k, v in missing.items() if v}
