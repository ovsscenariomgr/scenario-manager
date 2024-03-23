from django.db import models
from django.core.validators import MinValueValidator
from .Scene import Scene

class Timeout(models.Model):
    timeout_value = models.IntegerField(default=30, validators=[MinValueValidator(0)])
    scene_id = models.IntegerField(default=1, validators=[MinValueValidator(0)])
    # Foreign Key
    scenefk = models.OneToOneField(Scene, on_delete=models.CASCADE)