from django.db import models
from .Scenario import Scenario
from .File import File

class MediaFile(File):
    filename = models.FileField(upload_to='media', default='media/logo.jpeg')
    media = models.ForeignKey(Scenario, on_delete=models.CASCADE, related_name='media')