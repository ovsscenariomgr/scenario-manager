from django.db import models
from .Scenario import Scenario
from .File import File

# TODO: Need to add repeat, volume, play, mute?? per section 11.6 of spec?
class VocalFile(models.Model):
    # filename = models.FileField(upload_to='vocals', default='vocals/purr.wav')
    filename = models.CharField(max_length=256, default='vocals/purr.wav')
    title = models.CharField(max_length=256, default='Purr')
    scenario = models.ForeignKey(Scenario, on_delete=models.CASCADE, related_name='vocals')