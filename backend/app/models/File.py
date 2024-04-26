from django.db import models
from .Scenario import Scenario

# TODO: Need to add play? per section 11.6 of spec?
class MediaFile(models.Model):
    # filename = models.CharField(max_length=256, default='media/logo.jpeg')
    filename = models.FileField(upload_to='media', default='media/logo.jpeg')
    title = models.CharField(max_length=256, default='Logo')
    scenario = models.ForeignKey(Scenario, on_delete=models.CASCADE, related_name='media')

# TODO: Need to add repeat, volume, play, mute?? per section 11.6 of spec?
class VocalFile(models.Model):
    # filename = models.CharField(max_length=256, default='vocals/purr.wav')
    filename = models.FileField(upload_to='vocals', default='vocals/purr.wav')
    title = models.CharField(max_length=256, default='Purr')
    scenario = models.ForeignKey(Scenario, on_delete=models.CASCADE, related_name='vocals')