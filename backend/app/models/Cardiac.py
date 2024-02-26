from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from .Init import Init

RHYTHM_CHOICES=[
    ('sinus', 'Sinus rhythm'),
    ('afib', 'Atrial fibrillation'),
    ('vfib', 'Ventricular fibrillation'),
    ('vtach1', 'Ventricular tachycardia 1'),
    ('vtach2', 'Ventricular tachycardia 2'),
    ('ront', 'R-on-T'),
    ('asystole', 'Asystole'),
]

VPC_CHOICES=[
    ('none', 'None'),
    ('1-1', 'vtach1-singlet'),
    ('1-2', 'vtach1-couplet'),
    ('1-3', 'vtach1-triplet'),
    ('2-1', 'vtach2-singlet'),
    ('2-2', 'vtach2-couplet'),
    ('2-3', 'vtach2-triplet'),
    ('3-1', 'vtach3-singlet'),
    ('3-2', 'vtach3-couplet'),
    ('3-3', 'vtach3-triplet'),
]

VFIB_AMP_CHOICES=[('low', 'low'), ('medium', 'medium'), ('high', 'high'),]

PULSE_STRENGTH_CHOICES=[('none', 'none'), ('weak', 'weak'), ('medium', 'medium'), ('strong', 'strong'),]

HEART_SOUND_CHOICES=[
    ('normal', 'Normal'),
    ('systolic_murmur', 'Systolic Murmur'),
    ('pansystolic_murmur', 'Pansystolic Murmur'),
    ('holosystolic_murmur', 'Holosystolic Murmur'),
    ('continuous_murmur', 'Continuous Murmur'),
    ('diastolic_murmur', 'Diastolic Murmur'),
    ('gallop', 'Gallop')
]

ILLUMINATED_CHOICES=[(0, 'not illuminated'), (1, 'illuminated'),]

# TODO: Items indicated as trendable would need to associate a modifier: <transfer_time>100</transfer_time> somehow
class Cardiac(models.Model):
    rhythm = models.CharField(max_length=8, choices=RHYTHM_CHOICES, default=RHYTHM_CHOICES[0])
    vpc = models.CharField(max_length=4, choices=VPC_CHOICES, default=VPC_CHOICES[0])
    pea = models.IntegerField(default=0, choices=[(0, 'off'), (1, 'on')])
    vpc_freq = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(100)]) # in increments of 10, validate...
    vfib_amplitude = models.CharField(max_length=6, choices=VFIB_AMP_CHOICES, default=VFIB_AMP_CHOICES[0])
    rate = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(300)]) # Trendable
    nibp_rate = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(300)])
    bps_sys = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(300)]) # Trendable
    bps_dia = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(290)]) # Trendable
    left_dorsal_pulse_strength = models.CharField(max_length=6, choices=PULSE_STRENGTH_CHOICES, default=PULSE_STRENGTH_CHOICES[0])
    right_dorsal_pulse_strength = models.CharField(max_length=6, choices=PULSE_STRENGTH_CHOICES, default=PULSE_STRENGTH_CHOICES[0])
    left_femoral_pulse_strength = models.CharField(max_length=6, choices=PULSE_STRENGTH_CHOICES, default=PULSE_STRENGTH_CHOICES[0])
    right_dorsal_pulse_strength = models.CharField(max_length=6, choices=PULSE_STRENGTH_CHOICES, default=PULSE_STRENGTH_CHOICES[0])
    heart_sound_volume = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(10)])
    heart_sound = models.CharField(max_length=20, choices=HEART_SOUND_CHOICES, default=HEART_SOUND_CHOICES[0])
    ecg_indicator = models.IntegerField(choices=ILLUMINATED_CHOICES, default=ILLUMINATED_CHOICES[0])
    bp_cuff = models.IntegerField(choices=ILLUMINATED_CHOICES, default=ILLUMINATED_CHOICES[0])
    arrest = models.IntegerField(choices=ILLUMINATED_CHOICES, default=ILLUMINATED_CHOICES[0])


class InitCardiac(Cardiac):
    init = models.OneToOneField(Init, on_delete=models.CASCADE, related_name='cardiac')