from drf_writable_nested.serializers import WritableNestedModelSerializer
from app.models import Profile
from .AvatarSerializer import AvatarSerializer
from .ControlSerializer import ControlSerializer
from .SummarySerializer import SummarySerializer

class ProfileSerializer(WritableNestedModelSerializer):
    avatar = AvatarSerializer()
    summary = SummarySerializer()
    controls = ControlSerializer(many=True)

    class Meta:
        model = Profile
        fields = ('avatar', 'summary', 'controls', 'color')

    # TODO: deal with color in the to_internal_value when deserializing
    # and in the XMLParser to ingest existing XML
    # This will be a problem because it just ends up in the list as "#000000", which is fine for json,
    # but xml renderer needs help.    
    # def to_representation(self, instance):
    #     rep = super().to_representation(instance)
    #     color = rep.pop('color')
    #     rep['controls'].insert(1, color)
    #     return rep
    
    # TODO: to_internal_value()
    # def to_internal_value(self, data):
    #   return super(WritableNestedModelSerializer, self).to_internal_value(data)