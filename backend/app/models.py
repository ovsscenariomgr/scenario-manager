from django.db import models

# Create your models here.
class Scenario(models.Model):
    pass
class Header(models.Model):
    author = models.CharField(max_length=256)
    date_of_creation = models.DateField()
    description = models.TextField()
    scenario = models.OneToOneField(Scenario, on_delete=models.CASCADE)

class Title(models.Model):
    header = models.OneToOneField(Header, on_delete=models.CASCADE)
    name = models.CharField(max_length=256)
    top = models.IntegerField(default=0) # Distance from top in pixels
    left = models.IntegerField(default=0) # Distance from left in pixels