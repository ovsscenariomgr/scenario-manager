import re
import os
from io import BytesIO
from ..parsers import ScenarioXMLParser, OvsXMLParser
from .test_setup import TestSetup

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
        resp = self.client.post(self.scenario_list, self.xml, content_type='application/xml')
        self.assertEqual(resp.status_code, 201)
        parsed = ScenarioXMLParser().parse(BytesIO(resp.content))
        self.assertEqual(parsed['id'], 1)
        # Should be able to retrieve anonymously
        self.client.logout()
        resp = self.client.get(self.scenario_detail)
        self.assertEqual(resp.status_code, 200)

    def test_scenario_update(self):
        with open(os.path.join(os.path.dirname(__file__), 'updated.xml'), 'r+') as file:
            updated_xml = file.read()
        resp = self.client.post(self.scenario_list, self.xml, content_type='application/xml')
        self.assertEqual(resp.status_code, 201)
        resp = self.client.put(self.scenario_detail, updated_xml, content_type='application/xml')
        self.assertEqual(resp.status_code, 200)
        parsed = ScenarioXMLParser().parse(BytesIO(resp.content))
        self.assertEqual(parsed['header']['author'], 'new author')
        self.assertEqual(len(parsed['eventgroups'][0]['events']), 2)
        self.assertEqual(len(parsed['scenes']), 2)

    def test_add_vocal(self):
        resp = self.client.post(self.scenario_list, self.xml, content_type='application/xml')
        self.assertEqual(resp.status_code, 201)
        data = {'title': 'test', 'filename': self.wav_file}
        resp = self.client.put(self.scenario_vocals, data, format='multipart')
        self.assertEqual(resp.status_code, 201)
        self.assertEqual(resp.data['filename'], os.path.basename(data['filename'].name))
        self.assertEqual(resp.data['title'], data['title'])
        # Verify vocal added to scenario
        resp = self.client.get(self.scenario_detail)
        self.assertEqual(resp.status_code, 200)
        parsed = ScenarioXMLParser().parse(BytesIO(resp.content))
        self.assertEqual(len(parsed['vocalfiles']), 1)
        self.assertEqual(parsed['vocalfiles'][0]['title'], data['title'])
        self.assertEqual(parsed['vocalfiles'][0]['filename'], os.path.basename(data['filename'].name))

    def test_add_media(self):
        resp = self.client.post(self.scenario_list, self.xml, content_type='application/xml')
        self.assertEqual(resp.status_code, 201)
        data = {'title': 'test', 'filename': self.media_file}
        resp = self.client.put(self.scenario_media, data, format='multipart')
        self.assertEqual(resp.status_code, 201)
        self.assertEqual(resp.data['filename'], os.path.basename(data['filename'].name))
        self.assertEqual(resp.data['title'], data['title'])
        # Verify media added to scenario
        resp = self.client.get(self.scenario_detail)
        self.assertEqual(resp.status_code, 200)
        parsed = ScenarioXMLParser().parse(BytesIO(resp.content))
        self.assertEqual(len(parsed['mediafiles']), 1)
        self.assertEqual(parsed['mediafiles'][0]['title'], data['title'])
        self.assertEqual(parsed['mediafiles'][0]['filename'], os.path.basename(data['filename'].name))

    def test_add_images(self):
        resp = self.client.post(self.scenario_list, self.xml, content_type='application/xml')
        self.assertEqual(resp.status_code, 201)
        data = {'avatar': self.img_file, 'summary': self.img_file}
        resp = self.client.patch(self.scenario_images, data, format='multipart')
        self.assertEqual(resp.status_code, 200)
        parsed = ScenarioXMLParser().parse(BytesIO(resp.content))
        self.assertEqual(parsed['profile']['avatar']['filename'], os.path.basename(data['avatar'].name))
        self.assertEqual(parsed['profile']['summary']['image'], os.path.basename(data['summary'].name))

    def test_scenario_export(self):
        resp = self.client.post(self.scenario_list, self.xml, content_type='application/xml')
        self.assertEqual(resp.status_code, 201)
        # Export as OVS spec
        resp = self.client.get(self.scenario_export, content_type='application/ovsxml')
        self.assertEqual(resp.status_code, 200)
        parsed = OvsXMLParser().parse(BytesIO(resp.content))
        self.assertEqual(parsed['id'], 1)
        self.assertEqual(len(parsed['events']), 2)
        self.assertEqual(len(parsed['vocals']), 0)
        self.assertEqual(len(parsed['media']), 0)