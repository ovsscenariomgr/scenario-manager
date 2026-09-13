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
        self.serializer_data['init']['initial_scene'] = 99
        self.serializer_data['scenes'][0]['id'] = 1
        serializer = ScenarioSerializer(data=self.serializer_data)
        self.assertFalse(serializer.is_valid())
        self.assertIn('init', serializer.errors)

    def test_initial_scene_matching_a_real_scene_is_valid(self):
        self.serializer_data['init']['initial_scene'] = 1
        self.serializer_data['scenes'][0]['id'] = 1
        serializer = ScenarioSerializer(data=self.serializer_data)
        self.assertTrue(serializer.is_valid(), serializer.errors)

    def test_trigger_event_id_must_reference_a_real_event(self):
        self.serializer_data['eventgroups'] = [{'events': [{'id': 'dextrose', 'title': 'Dextrose'}]}]
        self.serializer_data['scenes'][0]['triggers'] = [{'event_id': 'nonexistent', 'scene_id': 2}]
        serializer = ScenarioSerializer(data=self.serializer_data)
        self.assertFalse(serializer.is_valid())
        self.assertIn('scenes', serializer.errors)

    def test_trigger_event_id_matching_a_real_event_is_valid(self):
        self.serializer_data['eventgroups'] = [{'events': [{'id': 'dextrose', 'title': 'Dextrose'}]}]
        self.serializer_data['scenes'][0]['triggers'] = [{'event_id': 'dextrose', 'scene_id': 2}]
        serializer = ScenarioSerializer(data=self.serializer_data)
        self.assertTrue(serializer.is_valid(), serializer.errors)