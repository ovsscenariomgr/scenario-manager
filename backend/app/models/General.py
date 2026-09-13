from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from .Init import ScenarioInit, SceneInit
from .Trigger import Trigger
from .CommonChoices import OnOffChoices

# TODO: Items indicated as trendable would need to associate a modifier: <transfer_time>100</transfer_time> somehow
class General(models.Model):
    temperature = models.IntegerField(default=975, validators=[MinValueValidator(0), MaxValueValidator(1100)]) # Trendable
    temperature_enable = models.IntegerField(choices=OnOffChoices.choices, default=OnOffChoices.OFF)

class ScenarioInitGeneral(General):
    scenario_init = models.OneToOneField(ScenarioInit, on_delete=models.CASCADE, related_name='general')

class SceneInitGeneral(General):
    scene_init = models.OneToOneField(SceneInit, on_delete=models.CASCADE, related_name='general')

class ParameterTriggerGeneral(General):
    trigger = models.OneToOneField(Trigger, on_delete=models.CASCADE, related_name='general', null=True, blank=True)