from rest_framework import serializers
from app.models import Cardiac, InitCardiac

class CardiacSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cardiac
        fields = '__all__'

class InitCardiacSerializer(CardiacSerializer):
    class Meta(CardiacSerializer.Meta):
        model = InitCardiac