from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from .Scenario import Scenario

class Init(models.Model):
    initial_scene = models.IntegerField()
    record = models.IntegerField()
    image = models.ImageField()
    # Foreign Key
    scenario = models.OneToOneField(Scenario, on_delete=models.CASCADE)