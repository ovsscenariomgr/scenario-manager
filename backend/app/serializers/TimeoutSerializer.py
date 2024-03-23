from rest_framework import serializers
from app.models import Timeout

class TimeoutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Timeout
        fields = ('timeout_value', 'scene_id',)