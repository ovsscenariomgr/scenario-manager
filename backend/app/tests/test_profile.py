from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase
from app.models import Scenario, Profile, Avatar, Summary, Control
from app.serializers import ProfileSerializer, AvatarSerializer, SummarySerializer, ControlSerializer

class ProfileTestCase(TestCase):
    def setUp(self) -> None:
        self.scenario = Scenario.objects.create()
        self.profile_attrs = {'color': 'black'}
        self.profile = Profile.objects.create(scenario=self.scenario, **self.profile_attrs)

        self.avatar_attrs = {'filename': 'image.jpg', 'height_pct': 50, 'width_pct': 50}
        self.avatar = Avatar.objects.create(profile=self.profile, **self.avatar_attrs)

        self.summary_attrs = {
            'description': 'test',
            'breed': 'beagle',
            'gender': 'male',
            'weight': '40kg',
            'species': 'canine',
            'symptoms': 'cough',
            'image': 'image.jpg'
        }
        self.summary = Summary.objects.create(profile=self.profile, **self.summary_attrs)

        self.control_attrs = {'title': 'vocals', 'id': 'vocals-dog-control', 'top': 50, 'left': 50}
        self.control = Control.objects.create(profile=self.profile, **self.control_attrs)

    def test_profile_serialization(self):
        serializer = ProfileSerializer(instance=self.profile)
        self.assertEqual(self.profile.color, serializer.data['color'])
        self.assertEqual(self.profile.avatar.height_pct, serializer.data['avatar']['height_pct'])
        self.assertEqual(self.profile.summary.species, serializer.data['summary']['species'])
        self.assertEqual(self.profile.controls.get().title, serializer.data['controls'][0]['title'])
        self.assertEqual(self.profile.scenario_id, self.scenario.id)
        self.assertEqual(self.avatar.profile_id, self.profile.id)
        self.assertEqual(self.summary.profile_id, self.profile.id)
        self.assertEqual(self.control.profile_id, self.profile.id)

    # def test_avatar_filefield(self):
    #     image_file = SimpleUploadedFile("test_image.jpg", b"file_content", content_type="image/jpeg")
    #     serializer_data = {'filename': image_file, 'height_pct': 10, 'width_pct': 10}
    #     serializer = AvatarSerializer(data=serializer_data)
    #     self.assertTrue(serializer.is_valid())

    def test_avatar_dimensions(self):
        serializer_data = {'filename': 'image.jpg', 'height_pct': 101, 'width_pct': -1}
        serializer = AvatarSerializer(data=serializer_data)
        self.assertFalse(serializer.is_valid())
        self.assertEqual(set(serializer.errors), set(['height_pct', 'width_pct']))

    def test_summary_required_fields(self):
        serializer_data = {"description": "test", "image": "image.jpg" }
        serializer = SummarySerializer(data=serializer_data)
        self.assertFalse(serializer.is_valid())
        self.assertEqual(set(serializer.errors), set(['breed', 'gender', 'weight', 'species']))

    def test_control_top_left(self):
        serializer_data = {'title': 'the title', 'id': 'vocals-dog-control', 'top': -1, 'left': -1}
        serializer = ControlSerializer(data=serializer_data)
        self.assertFalse(serializer.is_valid())
        self.assertEqual(set(serializer.errors), set(['top', 'left']))

    def test_control_id_invalid(self):
        serializer_data = {'title': 'the title', 'id': 'not-a-control', 'top': 0, 'left': 0}
        serializer = ControlSerializer(data=serializer_data)
        self.assertFalse(serializer.is_valid())
        self.assertEqual(set(serializer.errors), set(['id']))

    def test_control_id_valid(self):
        serializer_data = {'title': 'the title', 'id': 'left-femoral-pulse-dog-control', 'top': 0, 'left': 0}
        serializer = ControlSerializer(data=serializer_data)
        self.assertTrue(serializer.is_valid())