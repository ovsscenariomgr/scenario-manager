from rest_framework import serializers
from app.models import Trigger
from .CardiacSerializer import ParameterTriggerCardiacSerializer
from .RespirationSerializer import ParameterTriggerRespirationSerializer
from .GeneralSerializer import ParameterTriggerGeneralSerializer

class TriggerSerializer(serializers.ModelSerializer):
    cardiac = ParameterTriggerCardiacSerializer()
    respiration = ParameterTriggerRespirationSerializer()
    general = ParameterTriggerGeneralSerializer()

    class Meta:
        model = Trigger
        fields = ('group', 'scene_id', 'event_id', 'test', 'cpr_duration', 'cardiac', 'respiration', 'general',)