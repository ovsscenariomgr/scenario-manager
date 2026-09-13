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
    # A scene's init only overrides the parameters that change from the
    # scenario's initial state -- real archives commonly specify just one of
    # cardiac/respiration/general (e.g. main-sepsis.xml's scene 1 has only
    # <cardiac>), so none of the three should be required here.
    cardiac = SceneInitCardiacSerializer(required=False)
    respiration = SceneInitRespirationSerializer(required=False)
    general = SceneInitGeneralSerializer(required=False)

    class Meta:
        model = SceneInit
        fields = ('cardiac', 'respiration', 'general',)