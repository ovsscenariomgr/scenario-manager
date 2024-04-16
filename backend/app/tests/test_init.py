from django.test import TestCase
from app.models import Scenario, ScenarioInit, ScenarioInitCardiac, ScenarioInitRespiration, ScenarioInitGeneral
from app.serializers import ScenarioInitSerializer

class InitTestCase(TestCase):
    def setUp(self) -> None:
        self.scenario = Scenario.objects.create()
        self.scenario_init_attrs = {'initial_scene': 1, 'record': 0}
        self.scenario_init = ScenarioInit.objects.create(scenario=self.scenario, **self.scenario_init_attrs)

        self.scenario_init_cardiac_attrs = {}
        self.scenario_init_cardiac = ScenarioInitCardiac.objects.create(scenario_init=self.scenario_init, **self.scenario_init_cardiac_attrs)

        self.scenario_init_resp_attrs = {}
        self.scenario_init_resp = ScenarioInitRespiration.objects.create(scenario_init=self.scenario_init, **self.scenario_init_resp_attrs)

        self.scenario_init_gen_attrs = {}
        self.scenario_init_gen = ScenarioInitGeneral.objects.create(scenario_init=self.scenario_init, **self.scenario_init_gen_attrs)

    def test_scenario_init_serialization(self):
        serializer = ScenarioInitSerializer(instance=self.scenario_init)
        self.assertEqual(self.scenario_init.initial_scene, serializer.data['initial_scene'])
        self.assertEqual(self.scenario_init.record, serializer.data['record'])
        self.assertEqual(self.scenario_init.cardiac.rhythm, serializer.data['cardiac']['rhythm'])
        self.assertEqual(self.scenario_init.respiration.left_lung_sound, serializer.data['respiration']['left_lung_sound'])
        self.assertEqual(self.scenario_init.general.temperature, serializer.data['general']['temperature'])

    def test_required_fields(self):
        serializer_data = {'initial_scene': 1, 'record': 0}
        serializer = ScenarioInitSerializer(data=serializer_data)
        self.assertFalse(serializer.is_valid())
        self.assertEqual(set(serializer.errors), set(['cardiac', 'respiration', 'general']))

    def test_record_options(self):
        serializer_data = {'record': -1, 'cardiac': {}, 'respiration': {}, 'general': {}}
        serializer = ScenarioInitSerializer(data=serializer_data)
        self.assertFalse(serializer.is_valid())
        self.assertEqual(set(serializer.errors), set(['record']))

    def test_bad_cardiac_choices(self):
        choice_fields = ['rhythm', 'vpc', 'pea', 'vfib_amplitude', 'left_dorsal_pulse_strength', 'right_dorsal_pulse_strength',
            'left_femoral_pulse_strength', 'right_femoral_pulse_strength', 'heart_sound', 'ecg_indicator', 'bp_cuff', 'arrest']
        cardiac = dict.fromkeys(choice_fields, 'bad_choice')
        serializer_data = {'cardiac': cardiac, 'respiration': {}, 'general': {}}
        serializer = ScenarioInitSerializer(data=serializer_data)
        self.assertFalse(serializer.is_valid())
        self.assertEqual(set(serializer.errors['cardiac']), set(choice_fields))

    def test_cardiac_ranges_too_high(self):
        range_fields = [('vpc_freq', 101), ('rate', 301), ('nibp_rate', 301), ('bps_sys', 301), ('bps_dia', 291), ('heart_sound_volume', 11)]
        for field, value in range_fields:
            with self.subTest(msg='Bad Cardiac Range', field=field, value=value):
                cardiac = dict.fromkeys([field], value)
                serializer_data = {'cardiac': cardiac, 'respiration': {}, 'general': {}}
                serializer = ScenarioInitSerializer(data=serializer_data)
                self.assertFalse(serializer.is_valid())
                self.assertEqual(set(serializer.errors['cardiac']), set([field]))
                self.assertTrue(serializer.errors['cardiac'][field][0].title() == 'Ensure This Value Is Less Than Or Equal To %s.' % (value - 1))

    def test_cardiac_ranges_too_low(self):
        range_fields = ['vpc_freq', 'rate', 'nibp_rate', 'bps_sys', 'bps_dia', 'heart_sound_volume']
        cardiac = dict.fromkeys(range_fields, -1)
        serializer_data = {'cardiac': cardiac, 'respiration': {}, 'general': {}}
        serializer = ScenarioInitSerializer(data=serializer_data)
        self.assertFalse(serializer.is_valid())
        self.assertEqual(set(serializer.errors['cardiac']), set(range_fields))
        self.assertTrue(all([err[0].title() == 'Ensure This Value Is Greater Than Or Equal To 0.' for err in serializer.errors['cardiac'].values()]))

    def test_bad_resp_choices(self):
        choice_fields = ['left_lung_sound', 'right_lung_sound', 'spo2_indicator', 'etco2_indicator']
        resp = dict.fromkeys(choice_fields, 'bad_choice')
        serializer_data = {'cardiac': {}, 'respiration': resp, 'general': {}}
        serializer = ScenarioInitSerializer(data=serializer_data)
        self.assertFalse(serializer.is_valid())
        self.assertEqual(set(serializer.errors['respiration']), set(choice_fields))

    def test_resp_ranges_too_high(self):
        range_fields = [('left_lung_sound_volume', 11), ('right_lung_sound_volume', 11), ('spo2', 101), ('etco2', 151), ('rate', 61)]
        for field, value in range_fields:
            with self.subTest(msg='Bad Respiration Range', field=field, value=value):
                resp = dict.fromkeys([field], value)
                serializer_data = {'cardiac': {}, 'respiration': resp, 'general': {}}
                serializer = ScenarioInitSerializer(data=serializer_data)
                self.assertFalse(serializer.is_valid())
                self.assertEqual(set(serializer.errors['respiration']), set([field]))
                self.assertTrue(serializer.errors['respiration'][field][0].title() == 'Ensure This Value Is Less Than Or Equal To %s.' % (value - 1))

    def test_resp_ranges_too_low(self):
        range_fields = ['left_lung_sound_volume', 'right_lung_sound_volume', 'spo2', 'etco2', 'rate']
        resp = dict.fromkeys(range_fields, -1)
        serializer_data = {'cardiac': {}, 'respiration': resp, 'general': {}}
        serializer = ScenarioInitSerializer(data=serializer_data)
        self.assertFalse(serializer.is_valid())
        self.assertEqual(set(serializer.errors['respiration']), set(range_fields))
        self.assertTrue(all([err[0].title() == 'Ensure This Value Is Greater Than Or Equal To 0.' for err in serializer.errors['respiration'].values()]))

    def test_resp_lung_choices(self):
        choice_fields = [('left_lung_sound', 'same_as_left'), ('right_lung_sound', 'same_as_right')]
        for field, value in choice_fields:
            with self.subTest(msg='Lung sounds', field=field, value=value):
                resp = dict.fromkeys([field], value)
                serializer_data = {'cardiac': {}, 'respiration': resp, 'general': {}}
                serializer = ScenarioInitSerializer(data=serializer_data)
                self.assertFalse(serializer.is_valid())
                self.assertEqual(set(serializer.errors['respiration']), set([field]))
                self.assertTrue(str(serializer.errors['respiration'][field][0]) == 'Cannot be assigned value: %s' % (value))

    def test_bad_general_choices(self):
        serializer_data = {'cardiac': {}, 'respiration': {}, 'general': {'temperature_enable': 'bad_choice'}}
        serializer = ScenarioInitSerializer(data=serializer_data)
        self.assertFalse(serializer.is_valid())
        self.assertEqual(set(serializer.errors['general']), set(['temperature_enable']))

    def test_general_range_too_high(self):
        serializer_data = {'cardiac': {}, 'respiration': {}, 'general': {'temperature': 1101}}
        serializer = ScenarioInitSerializer(data=serializer_data)
        self.assertFalse(serializer.is_valid())
        self.assertEqual(set(serializer.errors['general']), set(['temperature']))
        self.assertTrue(serializer.errors['general']['temperature'][0].title() == 'Ensure This Value Is Less Than Or Equal To 1100.')        

    def test_general_range_too_low(self):
        serializer_data = {'cardiac': {}, 'respiration': {}, 'general': {'temperature': -1}}
        serializer = ScenarioInitSerializer(data=serializer_data)
        self.assertFalse(serializer.is_valid())
        self.assertEqual(set(serializer.errors['general']), set(['temperature']))
        self.assertTrue(serializer.errors['general']['temperature'][0].title() == 'Ensure This Value Is Greater Than Or Equal To 0.')
