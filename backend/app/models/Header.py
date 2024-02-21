from django.db import models
from django.utils.timezone import now
from .Scenario import Scenario

class Header(models.Model):
    author = models.CharField(max_length=256, default='ovsscenariomgr')
    date_of_creation = models.DateField(default=now)
    description = models.TextField(default='OVS Scenario Manager')
    # Foreign Key
    scenario = models.OneToOneField(Scenario, on_delete=models.CASCADE)