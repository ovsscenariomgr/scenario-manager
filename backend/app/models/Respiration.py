from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from .Init import ScenarioInit, SceneInit
from .Trigger import Trigger
from ..validators import validate_left_lung_sound, validate_right_lung_sound

# TODO: Items indicated as trendable would need to associate a modifier: <transfer_time>100</transfer_time> somehow
class Respiration(models.Model):
    class LungSoundChoices(models.TextChoices):
        NORMAL = 'normal'
        COARSE_CRACKLES = 'coarse_crackles'
        FINE_CRACKLES = 'fine_crackles'
        WHEEZES = 'wheezes'
        STRIDOR = 'stridor'
        STERTOR = 'stertor'
        SAME_AS_RIGHT = 'same_as_right'
        SAME_AS_LEFT = 'same_as_left'
    
    class ConnectedChoices(models.IntegerChoices):
        NOT_CONNECTED = 0
        CONNECTED = 1
    
    class MovementChoices(models.IntegerChoices):
        OFF = 0
        ON = 1

    left_lung_sound = models.CharField(max_length=16, choices=LungSoundChoices.choices, default=LungSoundChoices.NORMAL, validators=[validate_left_lung_sound])
    left_lung_sound_volume = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(10)])
    right_lung_sound = models.CharField(max_length=16, choices=LungSoundChoices.choices, default=LungSoundChoices.NORMAL, validators=[validate_right_lung_sound])
    right_lung_sound_volume = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(10)])
    inhalation_duration = models.IntegerField(default=500, validators=[MinValueValidator(0)])
    exhalation_duration = models.IntegerField(default=500, validators=[MinValueValidator(0)])
    spo2 = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(100)]) # Trendable
    spo2_indicator = models.IntegerField(default=ConnectedChoices.NOT_CONNECTED, choices=ConnectedChoices.choices)
    etco2 = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(150)]) # Trendable
    etco2_indicator = models.IntegerField(default=ConnectedChoices.NOT_CONNECTED, choices=ConnectedChoices.choices)
    rate = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(60)]) # Trendable
    chest_movement = models.IntegerField(default=MovementChoices.OFF, choices=MovementChoices.choices)

class ScenarioInitRespiration(Respiration):
    scenario_init = models.OneToOneField(ScenarioInit, on_delete=models.CASCADE, related_name='respiration')

class SceneInitRespiration(Respiration):
    scene_init = models.OneToOneField(SceneInit, on_delete=models.CASCADE, related_name='respiration')

class ParameterTriggerRespiration(Respiration):
    manual_count = models.IntegerField(default=0, validators=[MinValueValidator(0)]) # this is only for triggers..
    trigger = models.OneToOneField(Trigger, on_delete=models.CASCADE, related_name='respiration', null=True, blank=True)