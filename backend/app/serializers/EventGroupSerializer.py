from drf_writable_nested.serializers import WritableNestedModelSerializer
from app.models import EventGroup
from .EventSerializer import EventSerializer

class EventGroupSerializer(WritableNestedModelSerializer):
    events = EventSerializer(many=True)

    class Meta:
        model = EventGroup
        fields = ('name', 'title', 'events',)