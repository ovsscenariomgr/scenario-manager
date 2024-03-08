from rest_framework import serializers
from app.models import General, ScenarioInitGeneral, SceneInitGeneral

class GeneralSerializer(serializers.ModelSerializer):
    class Meta:
        model = General
        fields = ('temperature', 'temperature_enable',)

class ScenarioInitGeneralSerializer(GeneralSerializer):
    class Meta(GeneralSerializer.Meta):
        model = ScenarioInitGeneral

class SceneInitGeneralSerializer(GeneralSerializer):
    class Meta(GeneralSerializer.Meta):
        model = SceneInitGeneral