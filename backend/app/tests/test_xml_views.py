import re
import os
from .test_setup import TestSetup
xmlheaders={"accept": "application/xml"}
class TestXMLViews(TestSetup):

    def test_scenario_list(self):
        # Should work without being logged in
        self.client.logout()
        resp = self.client.get(self.scenario_list)
        self.assertContains(resp, '<?xml version="1.0" encoding="utf-8"?>\n<scenarios></scenarios>')

    def test_scenario_create_needs_auth(self):
        # Should not work without being logged in
        self.client.logout()
        resp = self.client.post(self.scenario_list, self.xml, content_type='application/xml')
        self.assertEqual(resp.status_code, 403)

    def test_scenario_create_without_data(self):
        resp = self.client.post(self.scenario_list, content_type='application/xml')
        self.assertEqual(resp.status_code, 400)

    def test_scenario_create_with_data(self):
        # NOTE: The fields order in the serializer effects render order, so the test.xml has to be in the same order for assertContains
        # TODO: replace this hacky shit with actual xml parse.
        expected = re.sub(r'[\n\t]*', '', self.xml).replace("<?xml version='1.0' encoding='utf-8'?><scenario>", '<scenario><id>1</id>')
        resp = self.client.post(self.scenario_list, self.xml, content_type='application/xml')
        # print(resp.content)
        self.assertContains(resp, expected, status_code=201)
        # Should be able to retrieve anonymously
        self.client.logout()
        resp = self.client.get(self.scenario_detail)
        self.assertContains(resp, expected)

    def test_scenario_update(self):
        # NOTE: The fields order in the serializer effects render order, so the test.xml has to be in the same order for assertContains
        # TODO: replace this hacky shit with actual xml parse.
        with open(os.path.join(os.path.dirname(__file__), 'updated.xml'), 'r+') as file:
            updated_xml = file.read()
        expected = re.sub(r'[\n\t]*', '', updated_xml).replace("<?xml version='1.0' encoding='utf-8'?><scenario>", '<scenario><id>1</id>')
        resp = self.client.post(self.scenario_list, self.xml, content_type='application/xml')
        # print(resp.content)
        self.assertEqual(resp.status_code, 201)
        resp = self.client.put(self.scenario_detail, updated_xml, content_type='application/xml')
        # print(resp.content)
        self.assertContains(resp, expected)