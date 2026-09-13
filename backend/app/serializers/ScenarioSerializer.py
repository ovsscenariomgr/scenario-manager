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

    def validate(self, data):
        scene_ids = {scene.get('id') for scene in data.get('scenes', []) if scene.get('id') is not None}
        event_ids = {
            event.get('id')
            for group in data.get('eventgroups', [])
            for event in group.get('events', [])
            if event.get('id')
        }

        initial_scene = data.get('init', {}).get('initial_scene')
        if initial_scene is not None and initial_scene not in scene_ids:
            raise serializers.ValidationError({
                'init': {'initial_scene': 'initial_scene %s does not match any scene id' % initial_scene}
            })

        for scene in data.get('scenes', []):
            for trigger in scene.get('triggers', []):
                event_id = trigger.get('event_id')
                if event_id and event_id not in event_ids:
                    raise serializers.ValidationError({
                        'scenes': 'trigger event_id "%s" does not match any event id' % event_id
                    })

        return data