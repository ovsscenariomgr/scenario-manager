from drf_writable_nested.serializers import WritableNestedModelSerializer
from app.models import Init
from .CardiacSerializer import InitCardiacSerializer
from .GeneralSerializer import InitGeneralSerializer
from .RespirationSerializer import InitRespirationSerializer

class InitSerializer(WritableNestedModelSerializer):
    cardiac = InitCardiacSerializer()
    respiration = InitRespirationSerializer()
    general = InitGeneralSerializer()

    class Meta:
        model = Init
        fields = ('cardiac', 'respiration', 'general', 'initial_scene', 'record',)