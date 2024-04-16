from django.db import models
from .Scenario import Scenario
from .Scene import Scene

class ScenarioInit(models.Model):

    class RecordChoices(models.IntegerChoices):
        OFF = 0
        ON = 1

    # cardiac = OneToOneField(ScenarioInitCardiac)
    # respiration = OneToOneField(ScenarioInitRespiration)
    # general = OneToOneField(ScenarioInitGeneral)
    initial_scene = models.IntegerField(default=1) # TODO: Validate that this scene id exists
    record = models.IntegerField(default=RecordChoices.OFF, choices=RecordChoices.choices)
    # Foreign Key
    scenario = models.OneToOneField(Scenario, on_delete=models.CASCADE, related_name='init')

class SceneInit(models.Model):
    # cardiac = OneToOneField(SceneInitCardiac)
    # respiration = OneToOneField(SceneInitRespiration)
    # general = OneToOneField(SceneInitGeneral)
    # Foreign Key
    scene = models.OneToOneField(Scene, on_delete=models.CASCADE, related_name='init')