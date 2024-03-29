from rest_framework import serializers
from app.models import Respiration, ScenarioInitRespiration, SceneInitRespiration, ParameterTriggerRespiration

class RespirationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Respiration
        fields = ('left_lung_sound','left_lung_sound_volume', 'right_lung_sound', 'right_lung_sound_volume', 'inhalation_duration',
                  'exhalation_duration', 'spo2', 'spo2_indicator', 'etco2', 'etco2_indicator', 'rate', 'chest_movement',)

class ScenarioInitRespirationSerializer(RespirationSerializer):
    class Meta(RespirationSerializer.Meta):
        model = ScenarioInitRespiration

class SceneInitRespirationSerializer(RespirationSerializer):
    class Meta(RespirationSerializer.Meta):
        model = SceneInitRespiration

class ParameterTriggerRespirationSerializer(RespirationSerializer):
    class Meta(RespirationSerializer.Meta):
        model = ParameterTriggerRespiration