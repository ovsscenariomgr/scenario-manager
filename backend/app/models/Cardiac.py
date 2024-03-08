from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from .Init import ScenarioInit, SceneInit

# TODO: Items indicated as trendable would need to associate a modifier: <transfer_time>100</transfer_time> somehow
class Cardiac(models.Model):
    class RhythmChoices(models.TextChoices):
        SINUS = 'sinus', 'Sinus rhythm'
        AFIB = 'afib', 'Atrial fibrillation'
        VFIB = 'vfib', 'Ventricular fibrillation'
        VTACH1 = 'vtach1', 'Ventricular tachycardia 1'
        VTACH2 = 'vtach2', 'Ventricular tachycardia 2'
        RONT = 'ront', 'R-on-T'
        ASYS = 'asystole', 'Asystole'
    
    class VpcChoices(models.TextChoices):
        NONE = 'none'
        VTACH1_SINGLET = '1-1' # Human readable name inferred from member name == Vtach1 Singlet
        VTACH1_COUPLET = '1-2'
        VTACH1_TRIPLET = '1-3'
        VTACH2_SINGLET = '2-1'
        VTACH2_COUPLET = '2-2'
        VTACH2_TRIPLET = '2-3'
        VTACH3_SINGLET = '3-1'
        VTACH3_COUPLET = '3-2'
        VTACH3_TRIPLET = '3-3'

    class PeaChoices(models.IntegerChoices):
        OFF = 0
        ON = 1

    class VfibAmpChoices(models.TextChoices):
        LOW = 'low'
        MEDIUM = 'medium'
        HIGH = 'high'

    class PulseStrengthChoices(models.TextChoices):
        NONE = 'none'
        WEAK = 'weak'
        MEDIUM = 'medium'
        STRONG = 'strong'

    class HeartSoundChoices(models.TextChoices):
        NORMAL = 'normal'
        SYSTOLIC_MURMUR = 'systolic_murmur'
        PANSYSTOLIC_MURMUR = 'pansystolic_murmur'
        HOLOSYSTOLIC_MURMUR = 'holosystolic_murmur'
        CONTINUOUS_MURMUR = 'continuous_murmur'
        DIASTOLIC_MURMUR = 'diastolic_murmur'
        GALLOP = 'gallop'
    
    class IlluminatedChoices(models.IntegerChoices):
        NOT_ILLUMINATED = 0
        ILLUMINATED = 1
    
    rhythm = models.CharField(max_length=8, choices=RhythmChoices.choices, default=RhythmChoices.SINUS)
    vpc = models.CharField(max_length=4, choices=VpcChoices.choices, default=VpcChoices.NONE)
    pea = models.IntegerField(choices=PeaChoices.choices, default=PeaChoices.OFF)
    vpc_freq = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(100)]) # in increments of 10, validate...
    vfib_amplitude = models.CharField(max_length=6, choices=VfibAmpChoices.choices, default=VfibAmpChoices.LOW)
    rate = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(300)]) # Trendable
    nibp_rate = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(300)])
    bps_sys = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(300)]) # Trendable
    bps_dia = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(290)]) # Trendable
    left_dorsal_pulse_strength = models.CharField(max_length=6, choices=PulseStrengthChoices.choices, default=PulseStrengthChoices.NONE)
    right_dorsal_pulse_strength = models.CharField(max_length=6, choices=PulseStrengthChoices.choices, default=PulseStrengthChoices.NONE)
    left_femoral_pulse_strength = models.CharField(max_length=6, choices=PulseStrengthChoices.choices, default=PulseStrengthChoices.NONE)
    right_femoral_pulse_strength = models.CharField(max_length=6, choices=PulseStrengthChoices.choices, default=PulseStrengthChoices.NONE)
    heart_sound_volume = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(10)])
    heart_sound = models.CharField(max_length=20, choices=HeartSoundChoices.choices, default=HeartSoundChoices.NORMAL)
    ecg_indicator = models.IntegerField(choices=IlluminatedChoices.choices, default=IlluminatedChoices.NOT_ILLUMINATED)
    bp_cuff = models.IntegerField(choices=IlluminatedChoices.choices, default=IlluminatedChoices.NOT_ILLUMINATED)
    arrest = models.IntegerField(choices=IlluminatedChoices.choices, default=IlluminatedChoices.NOT_ILLUMINATED)

class ScenarioInitCardiac(Cardiac):
    scenario_init = models.OneToOneField(ScenarioInit, on_delete=models.CASCADE, related_name='cardiac')

class SceneInitCardiac(Cardiac):
    scene_init = models.OneToOneField(SceneInit, on_delete=models.CASCADE, related_name='cardiac')