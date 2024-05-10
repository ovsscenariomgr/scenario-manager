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
        fields = ('avatar', 'summary', 'controls', 'color') # Color is added to controls list in the OvsXMLRenderer