from io import StringIO
from rest_framework_xml.renderers import XMLRenderer
from django.utils.encoding import force_str
from django.utils.xmlutils import SimplerXMLGenerator

class ScenarioXMLRenderer(XMLRenderer):
    """
    Renderer which serializes to XML.
    """
    root_tag_name = "scenario"
    singular_key_map = {}

    def render(self, data, accepted_media_type=None, renderer_context=None):
        """
        Renders `data` into serialized XML.
        """
        if data is None:
            return ""

        # A list of scenarios is rendered with plural root tag.
        render_root_tag = self.root_tag_name + 's' if isinstance(data, (list, tuple)) else self.root_tag_name

        stream = StringIO()

        xml = SimplerXMLGenerator(stream, self.charset)
        xml.startDocument()
        xml.startElement(render_root_tag, {})

        self._to_xml(xml, data, render_root_tag)

        xml.endElement(render_root_tag)
        xml.endDocument()
        return stream.getvalue()

    def _singular_key(self, key):
        # creates list like <controls><control>...</control></controls>
        return self.singular_key_map.get(key, key[:-1])

    def _startElement(self, xml, key, attrs):
        xml.startElement(key, attrs)

    def _endElement(self, xml, key):
        xml.endElement(key)

    def _to_xml(self, xml, data, key=None):
        if isinstance(data, (list, tuple)):
            for item in data:
                xml.startElement(self._singular_key(key), {})
                self._to_xml(xml, item)
                xml.endElement(self._singular_key(key))

        elif isinstance(data, dict):
            for key, value in data.items():
                self._startElement(xml, key, {})
                self._to_xml(xml, value, key)
                self._endElement(xml, key)

        elif data is None:
            # Don't output any value
            pass

        else:
            xml.characters(force_str(data))

class OvsXMLRenderer(ScenarioXMLRenderer):
    """
    Renderer which serializes to XML.
    """
    media_type = "application/ovsxml"

    # OVS spec list item transaltions
    singular_key_map = {
        'vocalfiles': 'file',
        'mediafiles': 'file',
        'eventgroups': 'category'
    }

    # OVS spec foreign key translations in root
    ovs_key_map = {
        'eventgroups': 'events',
        'vocalfiles': 'vocals',
        'mediafiles': 'media'
    }
    
    # "Flatten" events and scenes when rendering to XML because OVS XML spec 1.9 is poorly designed.
    flatten_keys = ['events', 'scenes']
    
    def _startElement(self, xml, key, attrs):
        if key in self.flatten_keys:
            # Don't write out the start parent/plural tag for lists we want to "flatten"
            pass
        else:
            xml.startElement(self.ovs_key_map.get(key, key), attrs)

    def _endElement(self, xml, key):
        if key in self.flatten_keys:
            # Don't write out the end parent/plural tag for lists we want to "flatten"
            pass
        else:
            xml.endElement(self.ovs_key_map.get(key, key))