from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from app.storage import OverwriteStorage
from .Profile import Profile

class Avatar(models.Model):
    # filename = models.CharField(max_length=256, default='images/linus.jpg')
    filename = models.ImageField(upload_to='images', storage=OverwriteStorage(), null=True)
    height_pct = models.IntegerField(default=100, validators=[MinValueValidator(0), MaxValueValidator(100)]) # Rendered size percentage 0-100
    width_pct = models.IntegerField(default=100, validators=[MinValueValidator(0), MaxValueValidator(100)]) # Rendered size percentage 0-100
    # Foreign Key
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE)