from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from .Profile import Profile

class Control(models.Model):
    controlid = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=256)
    id = models.CharField(max_length=256)
    top = models.IntegerField(default=100, validators=[MinValueValidator(0), MaxValueValidator(100)]) # Rendered size percentage 0-100
    left = models.IntegerField(default=100, validators=[MinValueValidator(0), MaxValueValidator(100)]) # Rendered size percentage 0-100
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='controls')