from rest_framework_xml.renderers import XMLRenderer

class ScenarioXMLRenderer(XMLRenderer):
    """Override XML tag names."""

    root_tag_name = 'scenario'
    item_tag_name = 'scenario'