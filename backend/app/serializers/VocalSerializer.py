from app.models import VocalFile
from .FileSerializer import FileSerializer

class VocalSerializer(FileSerializer):
    class Meta(FileSerializer.Meta):
        model = VocalFile
