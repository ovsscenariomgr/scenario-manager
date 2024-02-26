from rest_framework import serializers
from app.models import Init
from .CardiacSerializer import InitCardiacSerializer
from .GeneralSerializer import InitGeneralSerializer
from .RespirationSerializer import InitRespirationSerializer

class InitSerializer(serializers.ModelSerializer):
    cardiac = InitCardiacSerializer()
    respiration = InitRespirationSerializer()
    general = InitGeneralSerializer()

    class Meta:
        model = Init
        fields = ('cardiac', 'respiration', 'general', 'initial_scene', 'record',)