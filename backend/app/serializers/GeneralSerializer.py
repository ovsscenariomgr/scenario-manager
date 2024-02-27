from rest_framework import serializers
from app.models import General, InitGeneral

class GeneralSerializer(serializers.ModelSerializer):
    class Meta:
        model = General
        fields = ('temperature', 'temperature_enable',)

class InitGeneralSerializer(GeneralSerializer):
    class Meta(GeneralSerializer.Meta):
        model = InitGeneral