from django.db import models
from django.utils.timezone import now
from .Scenario import Scenario

class Header(models.Model):
    author = models.CharField(max_length=256, default='ovsscenariomgr')
    # title = OneToOneField(Title)
    date_of_creation = models.DateField(default=now)
    description = models.TextField(default='An Open Vet Sim scenario created by OVS Scenario Manager')
    # Foreign Key
    scenario = models.OneToOneField(Scenario, on_delete=models.CASCADE)