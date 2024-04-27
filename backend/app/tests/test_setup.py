import os
import glob
import json
import io
from PIL import Image
from pathlib import Path
from django.core.files.uploadedfile import SimpleUploadedFile
from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework.test import APITestCase

def generate_image_bytes():
    file = io.BytesIO()
    image = Image.new('RGBA', size=(1, 1), color=(0, 0, 0))
    image.save(file, 'png')
    file.name = 'test.png'
    file.seek(0)
    return file.read()

def generate_wav_bytes():
    return b'RIFF$\x00\x00\x00WAVEfmt \x10\x00\x00\x00\x01\x00\x01\x00\x00\x04\x00\x00\x00\x04\x00\x00\x01\x00\x08\x00data\x00\x00\x00\x00'

class TestSetup(APITestCase):
    def setUp(self):
        self.scenario_list = reverse('scenario_list')
        self.scenario_detail = reverse('scenario_detail', kwargs={'pk': 1})
        self.scenario_vocals = reverse('scenario_vocals', kwargs={'pk': 1})
        self.scenario_media = reverse('scenario_media', kwargs={'pk': 1})

        self.img_file = SimpleUploadedFile(name='test.jpg', content=generate_image_bytes(), content_type='multipart/form-data')
        self.wav_file = SimpleUploadedFile(name='test.wav', content=generate_wav_bytes(), content_type='multipart/form-data')
        self.media_file = SimpleUploadedFile(name='test.txt', content=b'test', content_type='multipart/form-data')

        self.user = User.objects.create_user(username='test', password='test')
        self.client.login(username='test', password='test')

        with open(os.path.join(os.path.dirname(__file__), 'test.json'), 'r+') as file:
            self.json = json.loads(file.read())
        with open(os.path.join(os.path.dirname(__file__), 'test.xml'), 'r+') as file:
            self.xml = file.read()
        return super().setUp()
    
    def tearDown(self):
        for dir in ['images', 'media', 'vocals']:
            file_dir = Path(__file__).resolve().parent.parent.parent.joinpath('files', dir)
            files = glob.glob(os.path.join(file_dir, 'test.*'))
            for f in files:
                os.remove(f)

        return super().tearDown()