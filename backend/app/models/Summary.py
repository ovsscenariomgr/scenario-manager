from django.db import models
from .Profile import Profile

class Summary(models.Model):
    description = models.TextField(default='Summary Description')
    breed = models.CharField(max_length=64, default='Dalmation') # Make this a choices field?
    gender = models.CharField(max_length=64, default='Male') # Make this a choices field?
    weight = models.CharField(max_length=6, default='30 kg')
    species = models.CharField(max_length=64, default='Canine') # Make this a choices field?
    symptoms = models.TextField(default='Summary Symptoms')
    image = models.CharField(max_length=256, default='summaryimage.jpg') # TODO: validate that this file exists??
    # Foreign Key
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE)