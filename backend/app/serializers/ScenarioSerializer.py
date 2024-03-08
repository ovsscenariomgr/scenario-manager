from drf_writable_nested.serializers import WritableNestedModelSerializer
from app.models import Scenario
from .CategorySerializer import CategorySerializer
from .HeaderSerializer import HeaderSerializer
from .FileSerializer import MediaSerializer, VocalSerializer
from .ProfileSerializer import ProfileSerializer
from .InitSerializer import ScenarioInitSerializer

class ScenarioSerializer(WritableNestedModelSerializer):
    header = HeaderSerializer()
    profile = ProfileSerializer()
    vocals = VocalSerializer(many=True)
    media = MediaSerializer(many=True)
    init = ScenarioInitSerializer()
    categories = CategorySerializer(many=True)

    class Meta:
        model = Scenario
        fields = ('id', 'header', 'profile', 'vocals', 'media', 'init', 'categories',)
