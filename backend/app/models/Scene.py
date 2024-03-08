from django.db import models

class Scene(models.Model):
    sceneid = models.BigAutoField(primary_key=True)

    title = models.CharField(max_length=256)
    id = models.IntegerField()
    
