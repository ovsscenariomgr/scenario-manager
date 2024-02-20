import re, os
from .test_setup import TestSetup
xmlheaders={"accept": "application/xml"}
class TestXMLViews(TestSetup):

    def test_scenario_list(self):
        resp = self.client.get(self.scenario_list, headers=xmlheaders)
        expected=b'''<?xml version="1.0" encoding="utf-8"?>\n<root></root>'''
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.content, expected)

    def test_scenario_create_without_data(self):
        resp = self.client.post(self.scenario_list, headers=xmlheaders)
        self.assertEqual(resp.status_code, 400)

    def test_scenario_create_with_data(self):
        # TODO: replace this hacky shit with actual xml parse.
        # Need to s/root/scenario as well
        expected = re.sub(r'[\n\t]*', '', self.xml).replace("<?xml version='1.0' encoding='utf-8'?><root>", '<root><id>1</id>')
        resp = self.client.post(self.scenario_list, self.xml, content_type='application/xml')
        self.assertContains(resp, expected, status_code=201)

    def test_scenario_update(self):
        # TODO: replace this hacky shit with actual xml parse.
        # Need to s/root/scenario as well in *.xml
        with open(os.path.join(os.path.dirname(__file__), 'updated.xml'), 'r+') as file:
            updated_xml = file.read()
        expected = re.sub(r'[\n\t]*', '', updated_xml).replace("<?xml version='1.0' encoding='utf-8'?><root>", '<root><id>1</id>')
        resp = self.client.post(self.scenario_list, self.xml, content_type='application/xml')
        self.assertEqual(resp.status_code, 201)
        resp = self.client.put(self.scenario_detail, updated_xml, content_type='application/xml')
        self.assertContains(resp, expected)