from rest_framework import serializers
from drf_writable_nested.serializers import WritableNestedModelSerializer
from app.models import Scenario
from .EventGroupSerializer import EventGroupSerializer
from .FileSerializer import MediaSerializer, VocalSerializer
from .HeaderSerializer import HeaderSerializer
from .InitSerializer import ScenarioInitSerializer
from .ProfileSerializer import ProfileSerializer
from .SceneSerializer import SceneSerializer

class ScenarioSerializer(WritableNestedModelSerializer):
    header = HeaderSerializer()
    profile = ProfileSerializer()
    vocals = VocalSerializer(many=True)
    media = MediaSerializer(many=True)
    init = ScenarioInitSerializer()
    eventgroups = EventGroupSerializer(many=True)
    scenes = SceneSerializer(many=True)

    class Meta:
        model = Scenario
        fields = ('id', 'header', 'profile', 'vocals', 'media', 'init', 'eventgroups', 'scenes',)

    # Categories == Events in rendered scenario xml
    def validate_eventgroups(self, value):
        if not len(value) > 0:
            raise serializers.ValidationError('eventgroups must contain at least one object')
        return value

    def validate_scenes(self, value):
        if not len(value) > 0:
            raise serializers.ValidationError('scenes must contain at least one object')
        return value