from django.db import models
from .Scenario import Scenario
from .Scene import Scene

class ScenarioInit(models.Model):
    initial_scene = models.IntegerField(default=1)
    record = models.IntegerField(default=1)
    # Foreign Key
    scenario = models.OneToOneField(Scenario, on_delete=models.CASCADE, related_name='init')

class SceneInit(models.Model):
    # Foreign Key
    scene = models.OneToOneField(Scene, on_delete=models.CASCADE, related_name='init')