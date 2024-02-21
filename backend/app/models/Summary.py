from django.db import models
from .Profile import Profile

class Summary(models.Model):
    description = models.TextField()
    breed = models.CharField(max_length=64)
    gender = models.CharField(max_length=64)
    weight = models.CharField(max_length=64)
    species = models.CharField(max_length=64)
    symptoms = models.TextField()
    image = models.CharField(max_length=256) # TODO: validate that this file exists??
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE)