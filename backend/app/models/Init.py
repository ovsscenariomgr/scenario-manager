from django.db import models
from .Scenario import Scenario
from .Scene import Scene

class ScenarioInit(models.Model):
    # cardiac = OneToOneField(ScenarioInitCardiac)
    # respiration = OneToOneField(ScenarioInitRespiration)
    # general = OneToOneField(ScenarioInitGeneral)
    initial_scene = models.IntegerField(default=1)
    record = models.IntegerField(default=1)
    # Foreign Key
    scenario = models.OneToOneField(Scenario, on_delete=models.CASCADE, related_name='init')

class SceneInit(models.Model):
    # cardiac = OneToOneField(SceneInitCardiac)
    # respiration = OneToOneField(SceneInitRespiration)
    # general = OneToOneField(SceneInitGeneral)
    dummy_field = models.IntegerField(default=1)
    # Foreign Key
    # scene = models.OneToOneField(Scene, on_delete=models.CASCADE, related_name='init')