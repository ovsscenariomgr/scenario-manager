from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

LUNG_SOUND_CHOICES=[
    ('normal', 'Normal'),
    ('coarse_crackles', 'Course crackles'),
    ('fine_crackels', 'Fine crackles'),
    ('wheezes', 'Wheezes'),
    ('stridor', 'Stridor'),
    ('stertor', 'Stertor'),
]

# TODO: Items indicated as trendable would need to associate a modifier: <transfer_time>100</transfer_time> somehow
class Respiration(models.Model):
    left_lung_sound = models.CharField(max_length=16, choices=LUNG_SOUND_CHOICES + [('same_as_right', 'Same as right')], default=LUNG_SOUND_CHOICES[0])
    left_lung_sound_volume = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(10)])
    right_lung_sound = models.CharField(max_length=16, choices=LUNG_SOUND_CHOICES + [('same_as_left', 'Same as left')], default=LUNG_SOUND_CHOICES[0])
    right_lung_sound_volume = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(10)])
    inhalation_duration =  models.IntegerField(default=0, validators=[MinValueValidator(0)])
    exhalation_duration =  models.IntegerField(default=0, validators=[MinValueValidator(0)])
    spo2 = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(100)]) # Trendable
    etco2 = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(150)]) # Trendable
    rate = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(60)]) # Trendable
    spo2_indicator = models.IntegerField(default=0, choices=[(0, 'Not connected'), (1, 'connected')])
    etco2_indicator = models.IntegerField(default=0, choices=[(0, 'Not connected'), (1, 'connected')])
    chest_movement = models.IntegerField(default=0, choices=[(0, 'off'), (1, 'on')])
    manual_count = models.IntegerField(default=0, validators=[MinValueValidator(0)])