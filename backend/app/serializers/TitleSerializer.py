from app.models import Title
from rest_framework import serializers

class TitleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Title
        fields = ('name', 'top', 'left',)