import os
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase
from django.utils.timezone import now
from app.models import Scenario, VocalFile, MediaFile
from app.serializers import VocalSerializer, MediaSerializer
from .test_setup import generate_wav_bytes

class VocalMediaTestCase(TestCase):

    wavfile = SimpleUploadedFile("test.wav", generate_wav_bytes(), content_type='audio/x-wav')
    txtfile = SimpleUploadedFile("test.txt", b'test', content_type='text/plain')

    def setUp(self):
        self.scenario = Scenario.objects.create()
        self.vocal_attrs = {'title': 'Barking', 'filename': self.wavfile}
        self.vocal = VocalFile.objects.create(scenario=self.scenario, **self.vocal_attrs)
        self.media_attrs = {'title': 'X-Ray', 'filename': self.txtfile}
        self.media = MediaFile.objects.create(scenario=self.scenario, **self.media_attrs)

    def test_vocal_serialization(self):
        serializer = VocalSerializer(instance=self.vocal)
        self.assertEqual(self.vocal.title, serializer.data['title'])
        # TODO: this needs to assert the right vocals/scenario path
        self.assertEqual(os.path.basename(self.vocal.filename.name), os.path.basename(serializer.data['filename']))
        self.assertEqual(self.vocal.scenario_id, self.scenario.id)

    def test_vocal_deserialization(self):
        # This model is serializing the scenario parent/fk, unlike others.
        serializer_data = {'scenario': self.scenario.pk, 'title': 'test', 'filename': self.wavfile}
        serializer = VocalSerializer(data=serializer_data)
        self.assertTrue(serializer.is_valid())

    def test_media_serialization(self):
        serializer = MediaSerializer(instance=self.media)
        self.assertEqual(self.media.title, serializer.data['title'])
        # TODO: this needs to assert the right media/scenario path
        self.assertEqual(os.path.basename(self.media.filename.name), os.path.basename(serializer.data['filename']))
        self.assertEqual(self.media.scenario_id, self.scenario.id)

    def test_media_deserialization(self):
        # This model is serializing the scenario parent/fk, unlike others.
        serializer_data = {'scenario': self.scenario.pk, 'title': 'test', 'filename': self.txtfile}
        serializer = MediaSerializer(data=serializer_data)
        self.assertTrue(serializer.is_valid())