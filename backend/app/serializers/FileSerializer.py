from rest_framework import serializers
from app.models import MediaFile, VocalFile

class MediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = MediaFile
        fields = ('scenario', 'filename', 'title',)

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep.pop('scenario')
        return rep

class VocalSerializer(serializers.ModelSerializer):
    class Meta:
        model = VocalFile
        fields = ('scenario', 'filename', 'title',)

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep.pop('scenario')
        return rep