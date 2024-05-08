from rest_framework_xml.parsers import XMLParser

class ScenarioXMLParser(XMLParser):
    list_item_tags = ['vocalfile', 'mediafile', 'control', 'eventgroup', 'event', 'scene', 'trigger']

    def _xml_convert(self, element):
        """
        convert the xml `element` into the corresponding python object
        """

        children = list(element)

        if len(children) == 0:
            if element.tag in ['vocalfiles', 'mediafiles', 'controls', 'eventgroups', 'events', 'scenes', 'triggers']:
                return []
            return self._type_convert(element.text)
        else:
            # If the tag is in the list of scenario xml "lists", do the thing here.
            # if the first child tag is list-item means all children are list-item
            if children[0].tag in self.list_item_tags:
                data = []
                for child in children:
                    data.append(self._xml_convert(child))
            else:
                data = {}
                for child in children:
                    data[child.tag] = self._xml_convert(child)

            return data
        
class OvsXMLParser(XMLParser):
    list_item_tags = ['file', 'control', 'category', 'event', 'scene', 'trigger']

    def _xml_convert(self, element):
        """
        convert the xml `element` into the corresponding python object
        """

        children = list(element)

        if len(children) == 0:
            if element.tag in ['vocals', 'media', 'controls', 'events', 'scenes', 'triggers']:
                return []
            return self._type_convert(element.text)
        else:
            # If the tag is in the list of scenario xml "lists", do the thing here.
            # if the first child tag is list-item means all children are list-item
            if children[0].tag in self.list_item_tags:
                data = []
                for child in children:
                    data.append(self._xml_convert(child))
            else:
                data = {}
                for child in children:
                    data[child.tag] = self._xml_convert(child)

            return data