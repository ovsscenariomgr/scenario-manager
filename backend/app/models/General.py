from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from .Init import Init

# TODO: Items indicated as trendable would need to associate a modifier: <transfer_time>100</transfer_time> somehow
class General(models.Model):
    class TempEnableChoices(models.IntegerChoices):
        OFF = 0
        ON = 1

    temperature = models.IntegerField(default=975, validators=[MinValueValidator(0), MaxValueValidator(1100)]) # Trendable
    temperature_enable = models.IntegerField(choices=TempEnableChoices.choices, default=TempEnableChoices.OFF)

class InitGeneral(General):
    init = models.OneToOneField(Init, on_delete=models.CASCADE, related_name='general')