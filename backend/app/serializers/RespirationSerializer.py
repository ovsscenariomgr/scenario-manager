from rest_framework import serializers
from app.models import Respiration, InitRespiration

class RespirationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Respiration
        fields = ('left_lung_sound','left_lung_sound_volume', 'right_lung_sound', 'right_lung_sound_volume', 'inhalation_duration',
                  'exhalation_duration', 'spo2', 'spo2_indicator', 'etco2', 'etco2_indicator', 'rate', 'chest_movement',)

class InitRespirationSerializer(RespirationSerializer):
    class Meta(RespirationSerializer.Meta):
        model = InitRespiration