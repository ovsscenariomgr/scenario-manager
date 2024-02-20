from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework.test import APITestCase

class TestSetup(APITestCase):
    def setUp(self):
        self.scenario_list = reverse('scenario_list')
        self.scenario_detail = reverse('scenario_detail', kwargs={'pk': 1})
        self.user = User.objects.create_user(username='test', password='test')
        self.client.login(username='test', password='test')

        self.json = {
		    "header": {
			"author": "test",
            "title": {
				"name": "test",
				"top": 0,
				"left": 0
			},
			"date_of_creation": "2024-02-18",
			"description": "test"
		    }
	    }
        self.xml = '''<?xml version='1.0' encoding='UTF-8'?>
<scenario>
    <header>
        <author>Test Author</author>
        <title>
            <name>Sepsis</name>
            <top>5</top>
            <left>10</left>
        </title>
        <date_of_creation>2023-08-29</date_of_creation>
        <description>
            Scenario depicting a dog with septic pneumonia
        </description>
    </header>
</scenario>    
'''
        return super().setUp()
    
    def tearDown(self):
        return super().tearDown()