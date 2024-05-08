from django.db import models
from .EventGroup import EventGroup

class Event(models.Model):
    class PriorityChoices(models.IntegerChoices):
        PRIORITY = 1
        NON_PRIORITY = 0

    eventid = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=256, default='Morphine')
    id = models.CharField(max_length=256, default='opiate_morphine')
    # TODO: Can multiple events be priority 1?
    priority = models.IntegerField(default=PriorityChoices.NON_PRIORITY, choices=PriorityChoices.choices, null=True, blank=True)
    hotkey = models.CharField(max_length=1, default='', null=True, blank=True) # TODO: validation of hotkey?
    # ForeignKey
    # TODO: The XML spec should be:
    # <events><event>...</event></events>
    # But... it's not, so this will ultimately have to get flattened in the Renderer.
    eventgroup = models.ForeignKey(EventGroup, on_delete=models.CASCADE, related_name='events')