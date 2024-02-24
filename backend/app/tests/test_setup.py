import os, json
from pathlib import Path
from django.core.files.uploadedfile import SimpleUploadedFile
from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework.test import APITestCase

def replace_file_paths(json):
    image_path = Path(__file__).resolve().parent.parent.parent.joinpath('files', 'images', 'linus.jpg')
    media_path = Path(__file__).resolve().parent.parent.parent.joinpath('files', 'media', 'logo.jpeg')
    vocal_path = Path(__file__).resolve().parent.parent.parent.joinpath('files', 'vocals', 'purr.wav')
    json['profile']['avatar']['filename'] = SimpleUploadedFile(name='linus.jpg', content=open(image_path, 'rb').read(), content_type='image/jpeg')
    json['profile']['summary']['image'] = SimpleUploadedFile(name='linus.jpg', content=open(image_path, 'rb').read(), content_type='image/jpeg')
    for v in json['vocals']:
        v['filename'] = SimpleUploadedFile(name='purr.wav', content=open(vocal_path, 'rb').read(), content_type='audio/wav')
    for m in json['media']:
        m['filename'] = SimpleUploadedFile(name='logo.jpg', content=open(media_path, 'rb').read(), content_type='image/jpeg')

class TestSetup(APITestCase):
    def setUp(self):
        self.scenario_list = reverse('scenario_list')
        self.scenario_detail = reverse('scenario_detail', kwargs={'pk': 1})
        self.user = User.objects.create_user(username='test', password='test')
        self.client.login(username='test', password='test')

        with open(os.path.join(os.path.dirname(__file__), 'test.json'), 'r+') as file:
            self.json = json.loads(file.read())
            # replace_file_paths(self.json)
        with open(os.path.join(os.path.dirname(__file__), 'test.xml'), 'r+') as file:
            self.xml = file.read()
        return super().setUp()
    
    def tearDown(self):
        return super().tearDown()