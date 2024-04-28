import os
import json
from .test_setup import TestSetup

class TestJsonViews(TestSetup):
    def test_scenario_list(self):
        # Should work without being logged in
        self.client.logout()
        resp = self.client.get(self.scenario_list, format="json")
        self.assertEqual(resp.data, [])

    def test_scenario_create_needs_auth(self):
        # Should not work without being logged in
        self.client.logout()
        resp = self.client.post(self.scenario_list, self.json, format="json")
        self.assertEqual(resp.status_code, 403)

    def test_scenario_create_without_data(self):
        resp = self.client.post(self.scenario_list, format="json")
        self.assertEqual(resp.status_code, 400)

    def test_scenario_create_with_data(self):
        resp = self.client.post(self.scenario_list, self.json, format="json")
        self.assertEqual(resp.status_code, 201)
        self.assertEqual(resp.data, self.json | {'id': 1})
        # Should be able to retrieve anonymously
        self.client.logout()
        resp = self.client.get(self.scenario_detail, format="json")
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.data, self.json | {'id': 1})

    def test_scenario_update(self):
        with open(os.path.join(os.path.dirname(__file__), 'updated.json'), 'r+') as file:
            updated_data = json.loads(file.read())
        resp = self.client.post(self.scenario_list, self.json, format="json")
        self.assertEqual(resp.status_code, 201)
        resp = self.client.put(self.scenario_detail, updated_data, format="json")
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.data, updated_data | {'id': 1})

    def test_add_vocal(self):
        resp = self.client.post(self.scenario_list, self.json, format="json")
        self.assertEqual(resp.status_code, 201)
        self.assertEqual(resp.data, self.json | {'id': 1})
        data = {'title': 'Purrrrr', 'filename': self.wav_file}
        resp = self.client.put(self.scenario_vocals, data, format='multipart')
        self.assertEqual(resp.status_code, 201)
        self.assertEqual(resp.data['filename'], os.path.basename(data['filename'].name))
        self.assertEqual(resp.data['title'], data['title'])
        # Verify vocal added to scenario
        resp = self.client.get(self.scenario_detail, format="json")
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(len(resp.data['vocals']), 1)
        self.assertEqual(resp.data['vocals'][0]['title'], data['title'])
        self.assertEqual(resp.data['vocals'][0]['filename'], os.path.basename(data['filename'].name))

    def test_add_media(self):
        resp = self.client.post(self.scenario_list, self.json, format="json")
        self.assertEqual(resp.status_code, 201)
        self.assertEqual(resp.data, self.json | {'id': 1})
        data = {'title': 'Media', 'filename': self.media_file}
        resp = self.client.put(self.scenario_media, data, format='multipart')
        self.assertEqual(resp.status_code, 201)
        self.assertEqual(resp.data['filename'], os.path.basename(data['filename'].name))
        self.assertEqual(resp.data['title'], data['title'])
        # Verify vocal added to scenario
        resp = self.client.get(self.scenario_detail, format="json")
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(len(resp.data['media']), 1)
        self.assertEqual(resp.data['media'][0]['title'], data['title'])
        self.assertEqual(resp.data['media'][0]['filename'], os.path.basename(data['filename'].name))

    def test_add_images(self):
        resp = self.client.post(self.scenario_list, self.json, format="json")
        self.assertEqual(resp.status_code, 201)
        data = {'avatar': self.img_file, 'summary': self.img_file}
        resp = self.client.patch(self.scenario_images, data, format='multipart')
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.data['profile']['avatar']['filename'], os.path.basename(data['avatar'].name))
        self.assertEqual(resp.data['profile']['summary']['image'], os.path.basename(data['summary'].name))
