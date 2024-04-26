from rest_framework import serializers
from app.models import MediaFile, VocalFile

class MediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = MediaFile
        fields = ('filename', 'title',)

class VocalSerializer(serializers.ModelSerializer):
    class Meta:
        model = VocalFile
        fields = ('filename', 'title',)