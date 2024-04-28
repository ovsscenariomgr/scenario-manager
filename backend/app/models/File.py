from django.db import models
from .Scenario import Scenario
from app.storage import OverwriteStorage, media_upload_to, vocals_upload_to

# TODO: Need to add play? per section 11.6 of spec?
class MediaFile(models.Model):
    filename = models.FileField(upload_to=media_upload_to, storage=OverwriteStorage())
    title = models.CharField(max_length=256, default='Logo')
    scenario = models.ForeignKey(Scenario, on_delete=models.CASCADE, related_name='media')

# TODO: Need to add repeat, volume, play, mute?? per section 11.6 of spec?
class VocalFile(models.Model):
    filename = models.FileField(upload_to=vocals_upload_to, storage=OverwriteStorage())
    title = models.CharField(max_length=256, default='Purr')
    scenario = models.ForeignKey(Scenario, on_delete=models.CASCADE, related_name='vocals')