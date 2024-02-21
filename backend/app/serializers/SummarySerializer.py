from app.models import Summary
from rest_framework import serializers

class SummarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Summary
        fields = ('description', 'breed', 'gender', 'weight', 'species', 'symptoms', 'image',)