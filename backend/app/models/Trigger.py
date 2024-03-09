from django.db import models
from django.core.validators import MinValueValidator
from .Scene import Scene

# TODO: Will need to do a lot of work in to_representation() of Serializer...
class Trigger(models.Model):
    class TestChoices(models.TextChoices):
        EQ = 'eq'
        GT = 'gt'
        LT = 'lt'
        LTE = 'lte'
        GTE = 'gte'
        INSIDE = 'inside'
        OUTSIDE = 'outside'
        NONE = ''

    # Common for all triggers
    group = models.IntegerField(default=1)
    scene_id = models.IntegerField(default=1, validators=[MinValueValidator(0)])
    # Event Trigger
    event_id = models.CharField(max_length=64, default='aed')
    # Test only part of CPR or Parameter Trigger
    test = models.CharField(max_length=7, choices=TestChoices.choices, default=TestChoices.EQ)
    # CPR Duration # TODO: Will need to render as <cpr><duration></duration></cpr>
    cpr_duration = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    # Parameter trigger, these one to one fields are nullable.
    # cardiac = OneToOneField(ParameterTriggerCardiac)
    # respiration = OneToOneField(ParameterTriggerRespiration)
    # general = OneToOneField(ParameterTriggerGeneral)

    # Foreign Key
    scenefk = models.ForeignKey(Scene, on_delete=models.CASCADE, related_name='triggers')
