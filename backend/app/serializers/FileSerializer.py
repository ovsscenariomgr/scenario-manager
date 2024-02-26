from rest_framework import serializers
from app.models import File, MediaFile, VocalFile

class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = ('filename', 'title',)

class MediaSerializer(FileSerializer):
    class Meta(FileSerializer.Meta):
        model = MediaFile

class VocalSerializer(FileSerializer):
    class Meta(FileSerializer.Meta):
        model = VocalFile