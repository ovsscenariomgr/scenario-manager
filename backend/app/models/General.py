from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# TODO: Items indicated as trendable would need to associate a modifier: <transfer_time>100</transfer_time> somehow
class General(models.Model):
    temperature = models.IntegerField(default=975, validators=[MinValueValidator(0), MaxValueValidator(1100)]) # Trendablen 
    temperature_enable = models.IntegerField(default=0, choices=[(0, 'off'), (1, 'on')])