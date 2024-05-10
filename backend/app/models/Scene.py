from django.db import models
from django.core.validators import MinValueValidator
from .Scenario import Scenario

class Scene(models.Model):
    sceneid = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=256, default='Opening Scene')
    id = models.IntegerField(default=1, validators=[MinValueValidator(0)]) # Must be unique, but combined with the parent scenario...
    # init = OneToOneField(SceneInit)
    # timeout = OneToOneField(Timeout)
    triggers_needed = models.IntegerField(default=1, validators=[MinValueValidator(0)])
    # triggers = ForeignKey
    # ForeignKey
    # "flattened" in OvsXMLRenderer so <scenes></scenes> is removed.
    scenario = models.ForeignKey(Scenario, on_delete=models.CASCADE, related_name='scenes')