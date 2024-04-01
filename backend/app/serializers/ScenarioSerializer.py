from rest_framework import serializers
from drf_writable_nested.serializers import WritableNestedModelSerializer
from app.models import Scenario
from .CategorySerializer import CategorySerializer
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
    categories = CategorySerializer(many=True)
    scenes = SceneSerializer(many=True)

    class Meta:
        model = Scenario
        fields = ('id', 'header', 'profile', 'vocals', 'media', 'init', 'categories', 'scenes',)

    # Categories == Events in rendered scenario xml
    def validate_categories(self, value):
        if not len(value) > 0:
            raise serializers.ValidationError('categories/events must contain at least one object')
        return value

    def validate_scenes(self, value):
        if not len(value) > 0:
            raise serializers.ValidationError('scenes must contain at least one object')
        return value