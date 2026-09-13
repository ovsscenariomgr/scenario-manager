import zipfile
from io import BytesIO
from django.urls import reverse
from app.models import Scenario
from .test_setup import TestSetup, generate_image_bytes, generate_wav_bytes

MANIFEST = """<?xml version="1.0" encoding="UTF-8"?>
<scenario>
    <header>
        <author>Import Test</author>
        <title><name>Imported</name><top>5</top><left>10</left></title>
        <date_of_creation>2024-01-01</date_of_creation>
        <description>An imported scenario</description>
    </header>
    <profile>
        <avatar><filename>avatar.png</filename><height_pct>100</height_pct><width_pct>100</width_pct></avatar>
        <summary>
            <description>Summary</description>
            <breed>Beagle</breed>
            <weight>10kg</weight>
            <species>Canine</species>
            <image>summary.png</image>
        </summary>
        <controls>
            <color>#112233</color>
            <control><title>Vocalizations</title><id>vocals-dog-control</id><top>1</top><left>2</left></control>
            <control><title>CPR</title><id>button-cpr</id><top>3</top><left>4</left></control>
        </controls>
    </profile>
    <vocals>
        <file><filename>bark.wav</filename><title>Bark</title></file>
    </vocals>
    <media>
        <file><filename>xray.jpg</filename><title>X-Ray</title></file>
    </media>
    <init>
        <cardiac><rhythm>sinus</rhythm></cardiac>
        <respiration><left_lung_sound>normal</left_lung_sound></respiration>
        <general><temperature>975</temperature></general>
        <initial_scene>1</initial_scene>
        <record>0</record>
    </init>
    <events>
        <category>
            <name>drugs</name>
            <title>Drugs</title>
            <event><title>Dextrose</title><id>dextrose</id><priority>1</priority></event>
        </category>
    </events>
    <scene>
        <title>Opening</title>
        <id>1</id>
        <init><cardiac><rate>100</rate></cardiac></init>
        <triggers>
            <trigger><event_id>dextrose</event_id><scene_id>2</scene_id></trigger>
        </triggers>
    </scene>
    <scene>
        <title>Terminal</title>
        <id>2</id>
    </scene>
</scenario>
"""


def build_archive(manifest=MANIFEST, xml_name='main.xml', include_files=True):
    buf = BytesIO()
    with zipfile.ZipFile(buf, 'w') as zf:
        zf.writestr(xml_name, manifest)
        if include_files:
            zf.writestr('images/avatar.png', generate_image_bytes())
            zf.writestr('images/summary.png', generate_image_bytes())
            zf.writestr('vocals/bark.wav', generate_wav_bytes())
            zf.writestr('media/xray.jpg', b'fake media bytes')
    buf.seek(0)
    return buf


class ImportTestCase(TestSetup):

    def test_import_needs_auth(self):
        self.client.logout()
        resp = self.client.post(self.scenario_import, {'archive': build_archive()}, format='multipart')
        self.assertEqual(resp.status_code, 403)

    def test_import_happy_path(self):
        resp = self.client.post(self.scenario_import, {'archive': build_archive()}, format='multipart')
        self.assertEqual(resp.status_code, 201, resp.data)
        scenario = Scenario.objects.get(pk=resp.data['id'])
        self.assertEqual(scenario.header.author, 'Import Test')
        self.assertEqual(scenario.profile.controls.count(), 2)
        self.assertEqual(scenario.vocalfiles.count(), 1)
        self.assertEqual(scenario.mediafiles.count(), 1)
        self.assertEqual(scenario.scenes.count(), 2)
        # Terminal scene has neither triggers nor a timeout
        terminal = scenario.scenes.get(id=2)
        self.assertEqual(terminal.triggers.count(), 0)
        self.assertFalse(hasattr(terminal, 'timeout'))
        self.assertTrue(scenario.profile.avatar.filename.name.endswith('avatar.png'))
        self.assertTrue(scenario.profile.summary.image.name.endswith('summary.png'))

    def test_import_tolerates_renamed_manifest(self):
        resp = self.client.post(
            self.scenario_import,
            {'archive': build_archive(xml_name='scenario_export.xml')},
            format='multipart',
        )
        self.assertEqual(resp.status_code, 201, resp.data)

    def test_import_rejects_missing_referenced_file(self):
        resp = self.client.post(
            self.scenario_import,
            {'archive': build_archive(include_files=False)},
            format='multipart',
        )
        self.assertEqual(resp.status_code, 400)
        self.assertIn('missing', resp.data)
        self.assertEqual(Scenario.objects.count(), 0)

    def test_import_rejects_multiple_xml_files(self):
        buf = BytesIO()
        with zipfile.ZipFile(buf, 'w') as zf:
            zf.writestr('main.xml', MANIFEST)
            zf.writestr('extra.xml', MANIFEST)
        buf.seek(0)
        resp = self.client.post(self.scenario_import, {'archive': buf}, format='multipart')
        self.assertEqual(resp.status_code, 400)

    def test_import_rejects_non_zip(self):
        resp = self.client.post(
            self.scenario_import, {'archive': BytesIO(b'not a zip')}, format='multipart'
        )
        self.assertEqual(resp.status_code, 400)

    def test_export_then_import_round_trip(self):
        resp = self.client.post(self.scenario_list, self.xml, content_type='application/xml')
        self.assertEqual(resp.status_code, 201)
        img_data = {'avatar': self.img_file, 'summary': self.img_file}
        self.client.patch(self.scenario_images, img_data, format='multipart')
        self.client.put(self.scenario_media, {'title': 'test', 'filename': self.media_file}, format='multipart')
        self.client.put(self.scenario_vocals, {'title': 'test', 'filename': self.wav_file}, format='multipart')

        export_resp = self.client.get(self.scenario_export)
        self.assertEqual(export_resp.status_code, 200)

        import_resp = self.client.post(
            self.scenario_import,
            {'archive': BytesIO(export_resp.content)},
            format='multipart',
        )
        self.assertEqual(import_resp.status_code, 201, import_resp.data)

        original = Scenario.objects.get(pk=1)
        imported = Scenario.objects.get(pk=import_resp.data['id'])
        self.assertNotEqual(original.pk, imported.pk)
        self.assertEqual(original.header.author, imported.header.author)
        self.assertEqual(original.scenes.count(), imported.scenes.count())
        self.assertEqual(original.eventgroups.count(), imported.eventgroups.count())
        self.assertEqual(imported.vocalfiles.count(), 1)
        self.assertEqual(imported.mediafiles.count(), 1)
