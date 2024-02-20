import os, json
from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework.test import APITestCase

class TestSetup(APITestCase):
    def setUp(self):
        self.scenario_list = reverse('scenario_list')
        self.scenario_detail = reverse('scenario_detail', kwargs={'pk': 1})
        self.user = User.objects.create_user(username='test', password='test')
        self.client.login(username='test', password='test')

        with open(os.path.join(os.path.dirname(__file__), 'test.json'), 'r+') as file:
            self.json = json.loads(file.read())
        with open(os.path.join(os.path.dirname(__file__), 'test.xml'), 'r+') as file:
            self.xml = file.read()
        return super().setUp()
    
    def tearDown(self):
        return super().tearDown()