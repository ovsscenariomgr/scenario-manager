from django.db import models
from .Scenario import Scenario
from .File import File

class MediaFile(File):
    media = models.ForeignKey(Scenario, on_delete=models.CASCADE, related_name='media')