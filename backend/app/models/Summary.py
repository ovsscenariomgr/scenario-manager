from django.db import models
from app.storage import OverwriteStorage, image_upload_to
from .Profile import Profile

class Summary(models.Model):
    description = models.TextField(default='Scenario Summary')
    breed = models.CharField(max_length=64) # Make this a choices field?
    gender = models.CharField(max_length=64) # Make this a choices field?
    weight = models.CharField(max_length=6)
    species = models.CharField(max_length=64) # Make this a choices field?
    symptoms = models.TextField(default='Scenario Symptoms')
    image = models.ImageField(upload_to=image_upload_to, storage=OverwriteStorage(), null=True, blank=True)
    # Foreign Key
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE)