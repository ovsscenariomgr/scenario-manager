from drf_writable_nested.serializers import WritableNestedModelSerializer
from app.models import Trigger
from .CardiacSerializer import ParameterTriggerCardiacSerializer
from .RespirationSerializer import ParameterTriggerRespirationSerializer
from .GeneralSerializer import ParameterTriggerGeneralSerializer

class TriggerSerializer(WritableNestedModelSerializer):
    cardiac = ParameterTriggerCardiacSerializer(required=False)
    respiration = ParameterTriggerRespirationSerializer(required=False)
    general = ParameterTriggerGeneralSerializer(required=False)

    class Meta:
        model = Trigger
        fields = ('group', 'scene_id', 'event_id', 'test', 'cpr_duration', 'cardiac', 'respiration', 'general',)

    def to_internal_value(self, data):
        if 'cpr' in data and 'duration' in data['cpr']:
            cpr_duration = data['cpr']['duration']
            data['cpr_duration'] = cpr_duration
        return super(WritableNestedModelSerializer, self).to_internal_value(data)

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        try:
            # Nullable fields should not be serialized
            nullable_keys = ['group', 'event_id', 'test', 'cpr_duration', 'cardiac', 'respiration', 'general']
            [rep.pop(nulledkey) for nulledkey in nullable_keys if not rep[nulledkey]]
            # Turn cpr duration into a dict
            if 'cpr_duration' in rep and rep['cpr_duration'] > 0:
                duration = rep.pop('cpr_duration')
                rep['cpr'] = {'duration': duration}
        except KeyError:
            pass
        return rep