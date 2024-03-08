from rest_framework import serializers
from app.models import Event

class EventSerializer(serializers.ModelSerializer):

    class Meta:
        model = Event
        fields = ('title', 'id', 'priority', 'hotkey',)

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        try:
             # If hotkey is empty, don't serialize the field
            if not rep['hotkey']:
                rep.pop('hotkey')
        except KeyError:
            pass
        return rep