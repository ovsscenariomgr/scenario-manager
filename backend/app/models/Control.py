from django.db import models
from django.core.validators import MinValueValidator
from django.core.exceptions import ValidationError
from .Profile import Profile

ID_HR_VALUES = [
    'Vocalizations',
    'Right Lung Sound',
    'Left Lung Sound',
    'Left Femoral Pulse',
    'Right Femoral Pulse',
    'Left Dorsal Pulse',
    'Right Dorsal Pulse',
    'Heart Sounds',
    'Chest Movement',
    'CPR',
    'ECG',
    'SpO2',
    'ETCO2',
    'Cuff',
    'Palpate',
    'Temp'
]

ID_VALUES = [
    'vocals-dog-control',
    'right-lung-dog-control',
    'left-lung-dog-control',
    'left-femoral-pulse-dog-control',
    'right-femoral-pulse-dog-control',
    'left-dorsal-pulse-dog-control',
    'right-dorsal-pulse-dog-control',
    'heart-sound-dog-control',
    'chest-dog-control',
    'button-cpr',
    'button-ekg',
    'button-SpO2',
    'button-CO2',
    'button-cuff',
    'button-palpate',
    'button-Tperi'
]

TITLE_VALID_CHOICES=list(zip(ID_HR_VALUES, ID_HR_VALUES))
ID_VALID_CHOICES=list(zip(ID_VALUES, ID_HR_VALUES))

class Control(models.Model):
    controlid = models.BigAutoField(primary_key=True)
     # Should title be limited or not? Spec says it is free form...
    title = models.CharField(max_length=256, choices=TITLE_VALID_CHOICES, default=TITLE_VALID_CHOICES[0])
    id = models.CharField(max_length=256, choices=ID_VALID_CHOICES, default=ID_VALID_CHOICES[0])
    top = models.IntegerField(default=0, validators=[MinValueValidator(0)]) # Distance from top in pixels, should there be a max?
    left = models.IntegerField(default=0, validators=[MinValueValidator(0)]) # Distance from top in pixels, should there be a max?
    # Foreign Key
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='controls')

    def clean(self):
        # Title and ID should match... fight me.
        if ID_HR_VALUES.index(self.title) != ID_VALUES.index(self.id):
            raise ValidationError("title: %s and id: %s must match" % (self.title, self.id))