from django.test import TestCase
from django.utils.timezone import now
from app.models import Header, Title, Scenario
from app.serializers import HeaderSerializer

class HeaderTestCase(TestCase):
    def setUp(self):
        self.scenario = Scenario.objects.create()
        self.header_attrs = {
            'author': 'Adrian Tchaikovsky',
            'date_of_creation': now().date(),
            'description': 'Object Description'
        }
        self.header = Header.objects.create(scenario=self.scenario, **self.header_attrs)
        self.title_attrs = {'name': 'Title 1', 'top': 0, 'left': 0}
        self.title = Title.objects.create(header=self.header, **self.title_attrs)

        self.serializer_data = {
            'author': 'Orson Scott Card',
            'date_of_creation': '2024-03-12',
            'description': 'Serializer Description',
            'scenario': self.scenario.id,
            'title': {'name': 'Test 2', 'top': 50, 'left': 50},  # Nested title data
        }
    
    def test_header_serialization(self):
        serializer = HeaderSerializer(instance=self.header)
        self.assertEqual(self.header.author, serializer.data['author'])
        self.assertEqual(self.header.date_of_creation.isoformat(), serializer.data['date_of_creation'])
        self.assertEqual(self.header.description, serializer.data['description'])
        self.assertEqual(self.header.scenario_id, self.scenario.id)
 
    def test_nested_deserializer_validation(self):
        serializer = HeaderSerializer(data=self.serializer_data)
        self.assertTrue(serializer.is_valid())

    def test_nested_deserializer_title_required(self):
        self.serializer_data.pop('title')
        serializer = HeaderSerializer(data=self.serializer_data)
        self.assertFalse(serializer.is_valid())
        self.assertEqual(set(serializer.errors), set(['title']))
    
    def test_title_top_left(self):
        self.serializer_data['title'] = {'name': 'name', 'top': -1, 'left': -1}
        serializer = HeaderSerializer(data=self.serializer_data)
        self.assertFalse(serializer.is_valid())
        self.assertEqual(set(serializer.errors['title']), set(['top', 'left']))
    
    # TODO: save() throws NULL constraint because of Scenario parent missing???
    # def test_nested_deserializer_save(self):
    #     serializer = HeaderSerializer(data=self.serializer_data)
    #     serializer.is_valid(raise_exception=True)
    #     header_instance = serializer.save()
        
    #     self.assertIsNotNone(header_instance)
    #     self.assertEqual(header_instance.author, self.serializer_data['author'])
    #     self.assertEqual(header_instance.date_of_creation, self.serializer_data['date_of_creation'])
    #     self.assertEqual(header_instance.description, self.serializer_data['description'])
    #     self.assertEqual(header_instance.scenario, self.scenario)
        
    #     # Check if nested title is saved correctly
    #     nested_title = Title.objects.get(header=header_instance)
    #     self.assertEqual(nested_title.name, self.serializer_data['title']['name'])