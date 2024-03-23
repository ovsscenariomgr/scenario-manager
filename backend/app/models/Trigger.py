from django.db import models
from django.core.validators import MinValueValidator
from .Scene import Scene

# Extending this model to CPR, Event, and Parameter more desirable, but nested caused problems
# TODO: Validation upon save for fields.
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

    # A scene_id is required for all triggers
    scene_id = models.IntegerField(default=1, validators=[MinValueValidator(0)])
     # Trigger Group is not required, but common to CPR, Event, and Parameter triggers
    group = models.IntegerField(default=None, null=True, blank=True)
    # Event Trigger TODO: validation that the event given actually exists in the scenario
    event_id = models.CharField(max_length=64, default=None, null=True, blank=True)
    # Test only part of CPR or Parameter Trigger
    test = models.CharField(max_length=7, choices=TestChoices.choices, default=TestChoices.NONE, null=True, blank=True)
    # CPR Duration. Will render/parse as <cpr><duration></duration></cpr>
    cpr_duration = models.IntegerField(default=None, validators=[MinValueValidator(0)], null=True, blank=True)
    # Parameter trigger, these one to one fields are nullable.
    # cardiac = OneToOneField(ParameterTriggerCardiac, null=True)
    # respiration = OneToOneField(ParameterTriggerRespiration, null=True)
    # general = OneToOneField(ParameterTriggerGeneral, null=True)

    # Foreign Key
    scenefk = models.ForeignKey(Scene, on_delete=models.CASCADE, related_name='triggers')
