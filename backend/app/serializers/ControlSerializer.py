from app.models import Control
from rest_framework import serializers

class ControlSerializer(serializers.ModelSerializer):
    class Meta:
        model = Control
        fields = ('title', 'id', 'top', 'left',)