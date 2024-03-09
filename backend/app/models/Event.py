from django.db import models
from .Category import Category

class Event(models.Model):
    eventid = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=256, default='Morphine')
    id = models.CharField(max_length=256, default='opiate_morphine')
    priority = models.IntegerField(default=0) # nullable
    hotkey = models.CharField(max_length=1, blank=True, default='') # TODO: should this be null? understand blank/null/none bleh.
    # ForeignKey
    # TODO: The XML spec should be:
    # <events><event>...</event></events>
    # But... it's not, so this will ultimately have to get flattented in the Renderer.
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='events')