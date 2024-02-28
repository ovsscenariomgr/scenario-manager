from drf_writable_nested.serializers import WritableNestedModelSerializer
from app.models import Scenario
from .HeaderSerializer import HeaderSerializer
from .FileSerializer import MediaSerializer, VocalSerializer
from .ProfileSerializer import ProfileSerializer
from .InitSerializer import InitSerializer

class ScenarioSerializer(WritableNestedModelSerializer):
    header = HeaderSerializer()
    profile = ProfileSerializer()
    vocals = VocalSerializer(many=True)
    media = MediaSerializer(many=True)
    init = InitSerializer()

    class Meta:
        model = Scenario
        fields = ('id', 'header', 'profile', 'vocals', 'media', 'init',)
