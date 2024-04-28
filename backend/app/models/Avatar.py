from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from app.storage import OverwriteStorage, image_upload_to
from .Profile import Profile

class Avatar(models.Model):
    filename = models.ImageField(upload_to=image_upload_to, storage=OverwriteStorage(), null=True, blank=True)
    height_pct = models.IntegerField(default=100, validators=[MinValueValidator(0), MaxValueValidator(100)]) # Rendered size percentage 0-100
    width_pct = models.IntegerField(default=100, validators=[MinValueValidator(0), MaxValueValidator(100)]) # Rendered size percentage 0-100
    # Foreign Key
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE)