from django.db import models

class File(models.Model):
    filename = models.CharField(max_length=256, default='bark.wav')
    title = models.CharField(max_length=256, default='Barking')