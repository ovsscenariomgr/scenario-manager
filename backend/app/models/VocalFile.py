from django.db import models
from .Scenario import Scenario
from .File import File

class VocalFile(models.Model):
    # filename = models.FileField(upload_to='vocals', default='vocals/purr.wav')
    filename = models.CharField(max_length=256, default='vocals/purr.wav')
    title = models.CharField(max_length=256, default='Purr')
    vocals = models.ForeignKey(Scenario, on_delete=models.CASCADE, related_name='vocals')