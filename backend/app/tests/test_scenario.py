from django.test import TestCase
from django.utils.timezone import now
from app.models import Header, Title, Scenario
from app.serializers import ScenarioSerializer

class ScenarioTestCase(TestCase):
    def setUp(self):
        self.serializer_data = {
            'header': {
                'author': 'test',
                'title': {'name': 'test'}
            },
            'profile': {
                'avatar': {},
                'summary': {
                    'breed': 'beagle',
                    'gender': 'male',
                    'weight': '40kg',
                    'species': 'canine'
                },
                'controls': []
            },
            'vocalfiles': [],
            'mediafiles': [],
            'init': {
                'cardiac': {},
                'respiration': {},
                'general': {}
            },
            'eventgroups': [{
                'events': []
            }],
            'scenes': [{
                'timeout': {},
                'init': {
                    'cardiac': {},
                    'respiration': {},
                    'general': {}
                },
                'triggers': [{}]
            }]
        }

    def test_nested_deserializer_validation(self):
        serializer = ScenarioSerializer(data=self.serializer_data)
        self.assertTrue(serializer.is_valid())
        # serializer.is_valid()
        # print(serializer.validated_data)
        scenario_instance = serializer.save()
        self.assertIsNotNone(scenario_instance)
        self.assertEqual(scenario_instance.id, 1)

    def test_scenario_required_fields(self):
        keys = self.serializer_data.keys()
        serializer = ScenarioSerializer(data={})
        self.assertFalse(serializer.is_valid())
        self.assertEqual(set(serializer.errors), set(keys))

    def test_scenes_and_eventgroups_must_have_at_least_one(self):
        self.serializer_data['eventgroups'] = []
        self.serializer_data['scenes'] = []
        serializer = ScenarioSerializer(data=self.serializer_data)
        self.assertFalse(serializer.is_valid())
        self.assertEqual(set(serializer.errors), set(['eventgroups', 'scenes']))

    def test_initial_scene_exists(self):
        self.skipTest("TODO")