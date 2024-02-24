from django.db import models
from .Scenario import Scenario
from .File import File

class VocalFile(File):
    filename = models.FileField(upload_to='vocals', default='vocals/purr.wav')
    vocals = models.ForeignKey(Scenario, on_delete=models.CASCADE, related_name='vocals')