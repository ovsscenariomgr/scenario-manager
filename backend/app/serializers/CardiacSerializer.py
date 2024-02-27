from rest_framework import serializers
from app.models import Cardiac, InitCardiac

class CardiacSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cardiac
        fields = ('rhythm', 'vpc', 'pea', 'vpc_freq', 'vfib_amplitude', 'rate', 'nibp_rate', 'bps_sys', 'bps_dia',
                  'left_dorsal_pulse_strength', 'right_dorsal_pulse_strength', 'left_femoral_pulse_strength', 'right_femoral_pulse_strength',
                  'heart_sound_volume', 'heart_sound', 'ecg_indicator', 'bp_cuff', 'arrest',)

class InitCardiacSerializer(CardiacSerializer):
    class Meta(CardiacSerializer.Meta):
        model = InitCardiac