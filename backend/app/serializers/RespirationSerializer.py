from rest_framework import serializers
from app.models import Respiration, InitRespiration

class RespirationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Respiration
        fields = '__all__'

class InitRespirationSerializer(RespirationSerializer):
    class Meta(RespirationSerializer.Meta):
        model = InitRespiration