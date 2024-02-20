from django.db import models
from .Scenario import Scenario

class Header(models.Model):
    author = models.CharField(max_length=256)
    date_of_creation = models.DateField()
    description = models.TextField()
    scenario = models.OneToOneField(Scenario, on_delete=models.CASCADE)