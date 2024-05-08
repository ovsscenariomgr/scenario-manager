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
    vocalfiles = VocalSerializer(many=True) # rendered as 'vocals'
    mediafiles = MediaSerializer(many=True) # rendered as 'media'
    init = ScenarioInitSerializer()
    eventgroups = EventGroupSerializer(many=True) # rendered as 'events'
    scenes = SceneSerializer(many=True)

    class Meta:
        model = Scenario
        fields = ('id', 'header', 'profile', 'vocalfiles', 'mediafiles', 'init', 'eventgroups', 'scenes',)

    # Categories == Events in rendered scenario xml
    def validate_eventgroups(self, value):
        if not len(value) > 0:
            raise serializers.ValidationError('eventgroups must contain at least one object')
        return value

    def validate_scenes(self, value):
        if not len(value) > 0:
            raise serializers.ValidationError('scenes must contain at least one object')
        return value