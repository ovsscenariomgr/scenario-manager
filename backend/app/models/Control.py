from django.db import models
from django.core.validators import MinValueValidator
from django.core.exceptions import ValidationError
from .Profile import Profile

class Control(models.Model):
    class IdChoices(models.TextChoices):
        VOCALIZATIONS = 'vocals-dog-control'
        RIGHT_LUNG_SOUND = 'right-lung-dog-control'
        LEFT_LUNG_SOUND = 'left-lung-dog-control'
        LEFT_FEMORAL_PULSE = 'left-femoral-pulse-dog-control'
        RIGHT_FEMORAL_PULSE = 'right-femoral-pulse-dog-control'
        LEFT_DORSAL_PULSE = 'left-dorsal-pulse-dog-control'
        RIGHT_DORSAL_PULSE = 'right-dorsal-pulse-dog-control'
        HEART_SOUNDS = 'heart-sound-dog-control'
        CHEST_MOVEMENT = 'chest-dog-control'
        CPR = 'button-cpr'
        EKG = 'button-ekg'
        SPO2 = 'button-SpO2'
        ETCO2 = 'button-CO2'
        CUFF = 'button-cuff'
        PALPATE = 'button-palpate'
        TEMP = 'button-Tperi'

    controlid = models.BigAutoField(primary_key=True)
     # Should title be limited or not? Spec says it is free form...
    title = models.CharField(max_length=256, default=IdChoices.VOCALIZATIONS)
    id = models.CharField(max_length=256, choices=IdChoices.choices, default=IdChoices.VOCALIZATIONS)
    top = models.IntegerField(default=0, validators=[MinValueValidator(0)]) # Distance from top in pixels, should there be a max?
    left = models.IntegerField(default=0, validators=[MinValueValidator(0)]) # Distance from top in pixels, should there be a max?
    # Foreign Key
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='controls')

    # def clean(self):
    #     # Title and ID should match... fight me.
    #     if self.title != self.id:
    #         raise ValidationError("title: %s and id: %s must match" % (self.title, self.id))