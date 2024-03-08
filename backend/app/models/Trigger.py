from django.db import models

class Trigger(models.Model):
    group = models.IntegerField(default=None)
    scene_id = models.IntegerField()