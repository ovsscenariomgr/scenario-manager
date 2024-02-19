from drf_writable_nested.serializers import WritableNestedModelSerializer
from app.models import Scenario
from .HeaderSerializer import HeaderSerializer

class ScenarioSerializer(WritableNestedModelSerializer):
    header = HeaderSerializer()
    class Meta:
        model = Scenario
        fields = ('id', 'header',)
