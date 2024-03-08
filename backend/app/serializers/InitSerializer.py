from drf_writable_nested.serializers import WritableNestedModelSerializer
from app.models import ScenarioInit, SceneInit
from .CardiacSerializer import ScenarioInitCardiacSerializer, SceneInitCardiacSerializer
from .GeneralSerializer import ScenarioInitGeneralSerializer, SceneInitGeneralSerializer
from .RespirationSerializer import ScenarioInitRespirationSerializer, SceneInitRespirationSerializer

class ScenarioInitSerializer(WritableNestedModelSerializer):
    cardiac = ScenarioInitCardiacSerializer()
    respiration = ScenarioInitRespirationSerializer()
    general = ScenarioInitGeneralSerializer()

    class Meta:
        model = ScenarioInit
        fields = ('cardiac', 'respiration', 'general', 'initial_scene', 'record',)

class SceneInitSerializer(WritableNestedModelSerializer):
    cardiac = SceneInitCardiacSerializer()
    respiration = SceneInitRespirationSerializer()
    general = SceneInitGeneralSerializer()

    class Meta:
        model = SceneInit
        fields = ('cardiac', 'respiration', 'general',)