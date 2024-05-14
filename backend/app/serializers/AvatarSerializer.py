import os
from app.models import Avatar
from rest_framework import serializers

class AvatarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Avatar
        fields = ('filename', 'height_pct', 'width_pct',)

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        try:
             # If filename is empty, don't serialize the field
            if not rep['filename']:
                rep.pop('filename')
        except KeyError:
            pass
        return rep