from django.db import models
from .Scenario import Scenario
from ..validators import validate_html5_color

class Profile(models.Model):
    # This belongs in the Controls object, but putting it here the until can
    # figure out how to deal with the bad xml schema layout.
    color = models.CharField(max_length=7, default='#000000', validators=[validate_html5_color])
    # Foreign Key
    scenario = models.OneToOneField(Scenario, on_delete=models.CASCADE)