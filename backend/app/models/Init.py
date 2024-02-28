from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from .Scenario import Scenario

class Init(models.Model):
    initial_scene = models.IntegerField(default=1)
    record = models.IntegerField(default=1)
    # Foreign Key
    scenario = models.OneToOneField(Scenario, on_delete=models.CASCADE)