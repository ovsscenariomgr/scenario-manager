from drf_writable_nested.serializers import WritableNestedModelSerializer
from app.models import Scene
from .InitSerializer import SceneInitSerializer
from .TimeoutSerializer import TimeoutSerializer
from .TriggerSerializer import TriggerSerializer

class SceneSerializer(WritableNestedModelSerializer):
    # init = SceneInitSerializer()
    timeout = TimeoutSerializer()
    # triggers = TriggerSerializer(many=True)

    class Meta:
        model = Scene
        # fields = ('title', 'id', 'init', 'timeout', 'triggers_needed', 'triggers')
        fields = ('title', 'id', 'timeout', 'triggers_needed')