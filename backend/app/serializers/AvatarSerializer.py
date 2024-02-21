from app.models import Avatar
from rest_framework import serializers

class AvatarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Avatar
        fields = ('filename', 'height_pct', 'width_pct',)