from drf_writable_nested.serializers import WritableNestedModelSerializer
from app.models import Scenario
from .HeaderSerializer import HeaderSerializer
from .ProfileSerializer import ProfileSerializer

class ScenarioSerializer(WritableNestedModelSerializer):
    header = HeaderSerializer()
    profile = ProfileSerializer()
    class Meta:
        model = Scenario
        fields = ('id', 'header', 'profile',)
