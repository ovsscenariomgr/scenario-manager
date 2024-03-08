from io import StringIO
from rest_framework_xml.renderers import XMLRenderer
from django.utils.encoding import force_str
from django.utils.xmlutils import SimplerXMLGenerator

class ScenarioXMLRenderer(XMLRenderer):
    # Override XML tag names
    root_tag_name = "scenario"

    # item_tag_name is overridden by key value to _to_xml

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

    def _to_xml(self, xml, data, key=None):
        if isinstance(data, (list, tuple)):
            for item in data:
                # creates list like <controls><control>...</control></controls>
                if key in ['vocals', 'media']:
                    singular_key = 'file'
                elif key == 'categories': # This needs to be events
                    singular_key = 'category'
                else:
                    singular_key = key[:-1]
                xml.startElement(singular_key, {})
                self._to_xml(xml, item)
                xml.endElement(singular_key)

        elif isinstance(data, dict):
            for key, value in data.items():
                xml.startElement(key, {})
                self._to_xml(xml, value, key)
                xml.endElement(key)

        elif data is None:
            # Don't output any value
            pass

        else:
            xml.characters(force_str(data))
