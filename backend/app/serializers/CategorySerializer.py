from drf_writable_nested.serializers import WritableNestedModelSerializer
from app.models import Category
from .EventSerializer import EventSerializer

class CategorySerializer(WritableNestedModelSerializer):
    events = EventSerializer(many=True)

    class Meta:
        model = Category
        fields = ('name', 'title', 'events',)