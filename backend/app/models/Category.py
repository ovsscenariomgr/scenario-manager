from django.db import models
from .Scenario import Scenario

class Category(models.Model):
    name = models.CharField(max_length=64, default='drugs')
    title = models.CharField(max_length=64, default='Injected Drugs')
    # events = ForeignKey(Event)
    # Foreign Key
    # TODO: This will have to get rendered as 'events' in the end XML, change
    scenario = models.ForeignKey(Scenario, on_delete=models.CASCADE, related_name='categories')

    class Meta:  
        verbose_name_plural = 'categories'