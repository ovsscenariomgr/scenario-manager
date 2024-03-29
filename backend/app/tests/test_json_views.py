import os
import json
from .test_setup import TestSetup, replace_file_paths

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
            # replace_file_paths(updated_data)
        resp = self.client.post(self.scenario_list, self.json, format="json")
        self.assertEqual(resp.status_code, 201)
        resp = self.client.put(self.scenario_detail, updated_data, format="json")
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.data, updated_data | {'id': 1})
