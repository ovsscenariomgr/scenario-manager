from drf_writable_nested.serializers import WritableNestedModelSerializer
from app.models import Scene
from .InitSerializer import SceneInitSerializer
from .TimeoutSerializer import TimeoutSerializer
from .TriggerSerializer import TriggerSerializer

class SceneSerializer(WritableNestedModelSerializer):
    # A terminal scene (no outgoing transitions) has neither a timeout nor
    # any triggers -- confirmed against real scenario archives, e.g. the
    # closing scene of main-sepsis.xml has no <timeout> and no <triggers>.
    init = SceneInitSerializer(required=False)
    timeout = TimeoutSerializer(required=False)
    triggers = TriggerSerializer(many=True, required=False)

    class Meta:
        model = Scene
        fields = ('title', 'id', 'triggers_needed', 'timeout', 'init', 'triggers',)