from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from .Profile import Profile

class Avatar(models.Model):
    filename = models.CharField(max_length=256) # TODO: validate that this file exists??
    height_pct = models.IntegerField(default=100, validators=[MinValueValidator(0), MaxValueValidator(100)]) # Rendered size percentage 0-100
    width_pct = models.IntegerField(default=100, validators=[MinValueValidator(0), MaxValueValidator(100)]) # Rendered size percentage 0-100
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE)