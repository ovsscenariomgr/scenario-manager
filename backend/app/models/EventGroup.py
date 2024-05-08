from django.db import models
from .Scenario import Scenario

# This will be rendered as <category> in XML spec
class EventGroup(models.Model):
    name = models.CharField(max_length=64, default='drugs')
    title = models.CharField(max_length=64, default='Injected Drugs')
    # events = ForeignKey(Event)
    # Foreign Key
    # TODO: This will have to get rendered as 'events' in the end XML, change
    scenario = models.ForeignKey(Scenario, on_delete=models.CASCADE, related_name='eventgroups')