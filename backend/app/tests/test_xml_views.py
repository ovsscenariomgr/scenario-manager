from .test_setup import TestSetup

class TestXMLViews(TestSetup):
    headers={"content-type":"application/xml", "accept": "application/xml"}

    def test_scenario_list(self):
        resp = self.client.get(self.scenario_list, headers=self.headers)
        expected=b'''<?xml version="1.0" encoding="utf-8"?>\n<root></root>'''
        self.assertEqual(resp.content, expected)

    def test_scenario_create_without_data(self):
        resp = self.client.post(self.scenario_list, headers=self.headers)
        self.assertEqual(resp.status_code, 400)

    def test_scenario_create_with_data(self):        
        resp = self.client.post(self.scenario_list, self.xml, headers=self.headers)
        self.assertEqual(resp.status_code, 201)
        # self.assertGreaterEqual(resp.data.pop('id'), 0)
        # self.assertEqual(resp.content, self.json | {'id': 1})

    # def test_scenario_update(self):
    #     updated_data = {
	# 	    "header": {
	# 		    "title": {
	# 			    "name": "UPDATE",
	# 			    "top": 50,
	# 			    "left": 10
	# 		    },
	# 		"author": "UPDATE",
	# 		"date_of_creation": "2024-02-20",
	# 		"description": "test"
	# 	    }
	#     }
    #     resp = self.client.post(self.scenario_list, self.json, format="xml")
    #     self.assertEqual(resp.status_code, 201)
    #     resp = self.client.put(self.scenario_detail, updated_data, format="xml")
    #     self.assertEqual(resp.status_code, 200)
    #     self.assertEqual(resp.data, updated_data | {'id': 1})