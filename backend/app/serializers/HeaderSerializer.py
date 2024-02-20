from drf_writable_nested.serializers import WritableNestedModelSerializer
from app.models import Header
from .TitleSerializer import TitleSerializer

class HeaderSerializer(WritableNestedModelSerializer):
    title = TitleSerializer()
    class Meta:
        model = Header
        fields = ('author', 'title', 'date_of_creation', 'description',)