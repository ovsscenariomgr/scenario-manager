from django.db import models
from django.core.validators import MinValueValidator
from .Profile import Profile

class Control(models.Model):
    controlid = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=256)
    id = models.CharField(max_length=256)
    top = models.IntegerField(default=100, validators=[MinValueValidator(0)]) # Distance from top in pixels, should there be a max?
    left = models.IntegerField(default=100, validators=[MinValueValidator(0)]) # Distance from top in pixels, should there be a max?
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='controls')