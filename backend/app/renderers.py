from io import StringIO
from rest_framework_xml.renderers import XMLRenderer
from django.utils.encoding import force_str
from django.utils.xmlutils import SimplerXMLGenerator

class ScenarioXMLRenderer(XMLRenderer):
    # Override XML tag names
    root_tag_name = "scenario"
    item_tag_name = "scenario"

    def render(self, data, accepted_media_type=None, renderer_context=None):
        """
        Renders `data` into serialized XML.
        """
        if data is None:
            return ""

        # Only overriding render so a list of scenarios is rendered with plural root tag.
        if isinstance(data, (list, tuple)):
            self.root_tag_name += 's'

        stream = StringIO()

        xml = SimplerXMLGenerator(stream, self.charset)
        xml.startDocument()
        xml.startElement(self.root_tag_name, {})

        self._to_xml(xml, data)

        xml.endElement(self.root_tag_name)
        xml.endDocument()
        return stream.getvalue()