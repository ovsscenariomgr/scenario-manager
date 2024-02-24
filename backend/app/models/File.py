from django.db import models

class File(models.Model):
    title = models.CharField(max_length=256, default='Your File')