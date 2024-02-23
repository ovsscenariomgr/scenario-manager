from app.models import MediaFile
from .FileSerializer import FileSerializer

class MediaSerializer(FileSerializer):
    class Meta(FileSerializer.Meta):
        model = MediaFile