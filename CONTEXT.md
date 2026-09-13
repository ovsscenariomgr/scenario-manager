# Glossary

## Scenario Archive
The unit of exchange with the outside OpenVetSim world: a zip file containing exactly one XML manifest
(`main.xml`) plus three required directories — `images/`, `vocals/`, `media/` — even if some are empty.
Defined in OVS Scenario Specification v1.11 §2.2-2.5. This is what Import must accept and what Export
must produce to be spec-compliant; a bare XML file is not a Scenario Archive.

## Scenario XML (`main.xml`)
The single manifest file inside a [[Scenario Archive]] describing one scenario's header, profile, vocals/media
file lists, init state, events, and scenes. Must be named `main.xml`; per spec, a differently-named XML file
inside an archive gets renamed on import. Referred to as "OVS XML" in code (`OvsXMLRenderer`/`OvsXMLParser`),
as distinct from the app's own internal `ScenarioXMLRenderer`/`ScenarioXMLParser` wire format (see below).

## Scenario (DB model)
The Django `Scenario` model/row and its nested children (header, profile, init, eventgroups, scenes, ...) — the
live, relationally-editable representation this app stores and edits. Converted to/from [[Scenario XML]] via
`OvsXMLRenderer`/`OvsXMLParser` on export/import, and to/from the app's own internal JSON/XML wire format via
`ScenarioSerializer` + `ScenarioXMLRenderer`/`ScenarioXMLParser` for the app's own API.

## Avatar image / Summary image
The up-to-two files living in a [[Scenario Archive]]'s `images/` directory: the avatar file
(`<profile><avatar><filename>`) and the scenario-summary image (`<profile><summary><image>`). Referenced by
filename only inside the XML — the bytes live in `images/`.

## Vocals
`.wav` files in a [[Scenario Archive]]'s `vocals/` directory, listed in `<vocals><file><filename>` and played
through the "Vocalizations" control on the avatar. No min/max count, but the directory must exist even if empty.

## Media
Browser-renderable files (image, pdf, or other OS-browser-recognized format) in a [[Scenario Archive]]'s
`media/` directory, listed in `<media><file><filename>`. No min/max count, but the directory must exist even if
empty.
