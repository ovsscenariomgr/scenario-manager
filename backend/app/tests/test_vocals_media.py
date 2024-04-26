from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase
from django.utils.timezone import now
from app.models import Scenario, VocalFile, MediaFile
from app.serializers import VocalSerializer, MediaSerializer

class VocalMediaTestCase(TestCase):
    def setUp(self):
        self.scenario = Scenario.objects.create()
        self.vocal_attrs = {
            'title': 'Barking',
            'filename': 'bark.wav'
        }
        self.vocal = VocalFile.objects.create(scenario=self.scenario, **self.vocal_attrs)
        self.media_attrs = {
            'title': 'X-Ray',
            'filename': 'x-ray.pdf'
        }
        self.media = MediaFile.objects.create(scenario=self.scenario, **self.media_attrs)

    def test_vocal_serialization(self):
        serializer = VocalSerializer(instance=self.vocal)
        self.assertEqual(self.vocal.title, serializer.data['title'])
        self.assertEqual(self.vocal.scenario_id, self.scenario.id)

    def test_vocal_deserialization(self):
        content = b'RIFF$\x00\x00\x00WAVEfmt \x10\x00\x00\x00\x01\x00\x01\x00\x00\x04\x00\x00\x00\x04\x00\x00\x01\x00\x08\x00data\x00\x00\x00\x00'
        serializer_data = {'title': 'test', 'filename': SimpleUploadedFile("test.wav", content, content_type='audio/x-wav')}
        serializer = VocalSerializer(data=serializer_data)
        self.assertTrue(serializer.is_valid())

    def test_media_serialization(self):
        serializer = MediaSerializer(instance=self.media)
        self.assertEqual(self.media.title, serializer.data['title'])
        self.assertEqual(self.media.scenario_id, self.scenario.id)

    def test_media_deserialization(self):
        serializer_data = {'title': 'test', 'filename': SimpleUploadedFile("test.txt", b'test', content_type='text/plain')}
        serializer = MediaSerializer(data=serializer_data)
        self.assertTrue(serializer.is_valid())