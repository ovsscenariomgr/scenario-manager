import os
from app.models import Summary
from rest_framework import serializers

class SummarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Summary
        fields = ('description', 'breed', 'gender', 'weight', 'species', 'symptoms', 'image',)

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        try:
             # If image is empty, don't serialize the field
            if not rep['image']:
                rep.pop('image')
        except KeyError:
            pass
        return rep