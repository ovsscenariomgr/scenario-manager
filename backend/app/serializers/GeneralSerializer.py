from rest_framework import serializers
from app.models import General, ScenarioInitGeneral, SceneInitGeneral, ParameterTriggerGeneral

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

class ParameterTriggerGeneralSerializer(GeneralSerializer):
    class Meta(GeneralSerializer.Meta):
        model = ParameterTriggerGeneral