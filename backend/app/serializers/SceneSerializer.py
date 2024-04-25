from rest_framework import serializers
from drf_writable_nested.serializers import WritableNestedModelSerializer
from app.models import Scene
from .InitSerializer import SceneInitSerializer
from .TimeoutSerializer import TimeoutSerializer
from .TriggerSerializer import TriggerSerializer

class SceneSerializer(WritableNestedModelSerializer):
    init = SceneInitSerializer()
    timeout = TimeoutSerializer()
    triggers = TriggerSerializer(many=True)

    class Meta:
        model = Scene
        fields = ('title', 'id', 'triggers_needed', 'timeout', 'init', 'triggers',)

    def validate_triggers(self, value):
        if not len(value) > 0:
            raise serializers.ValidationError('triggers must contain at least one object')
        return value