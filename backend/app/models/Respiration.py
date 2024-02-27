from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.exceptions import ValidationError
from .Init import Init

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

    left_lung_sound = models.CharField(max_length=16, choices=LungSoundChoices.choices, default=LungSoundChoices.NORMAL)
    left_lung_sound_volume = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(10)])
    right_lung_sound = models.CharField(max_length=16, choices=LungSoundChoices.choices, default=LungSoundChoices.NORMAL)
    right_lung_sound_volume = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(10)])
    inhalation_duration = models.IntegerField(default=500, validators=[MinValueValidator(0)])
    exhalation_duration = models.IntegerField(default=500, validators=[MinValueValidator(0)])
    spo2 = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(100)]) # Trendable
    spo2_indicator = models.IntegerField(default=ConnectedChoices.NOT_CONNECTED, choices=ConnectedChoices.choices)
    etco2 = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(150)]) # Trendable
    etco2_indicator = models.IntegerField(default=ConnectedChoices.NOT_CONNECTED, choices=ConnectedChoices.choices)
    rate = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(60)]) # Trendable
    chest_movement = models.IntegerField(default=MovementChoices.OFF, choices=MovementChoices.choices)
    # manual_count = models.IntegerField(default=0, validators=[MinValueValidator(0)]) # is this just an api field? or part of xml spec

    def clean(self):
        if self.left_lung_sound == self.LungSoundChoices.SAME_AS_LEFT:
            raise ValidationError("left_lung_sound cannot be assigned value: %s" % (self.LungSoundChoices.SAME_AS_LEFT))
        if self.right_lung_sound == self.LungSoundChoices.SAME_AS_RIGHT:
            raise ValidationError("right_lung_sound cannot be assigned value: %s" % (self.LungSoundChoices.SAME_AS_RIGHT))

class InitRespiration(Respiration):
    init = models.OneToOneField(Init, on_delete=models.CASCADE, related_name='respiration')