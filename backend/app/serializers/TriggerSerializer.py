from rest_framework import serializers
from app.models import Trigger

class TriggerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trigger
        fields = ('group', 'scene_id', 'event_id', 'test', 'cpr_duration', 'cardiac', 'respiration', 'general',)