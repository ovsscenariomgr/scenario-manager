import base64
from rest_framework.test import APITestCase
from django.urls import reverse
from django.contrib.auth.models import User
from app.serializers import ScenarioSerializer


class TestSetup(APITestCase):
    def setUp(self):
        self.scenario_list = reverse('scenario_list')
        self.scenario_detail = reverse('scenario_detail', kwargs={'pk': 1})
        self.user = User.objects.create_user(username='test', password='test')
        self.client.login(username='test', password='test')
        # self.client.credentials(HTTP_AUTHORIZATION='Basic %s' % base64.b64decode(b'admin:admin'))

        self.data = {
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
        return super().setUp()
    
    def tearDown(self):
        return super().tearDown()