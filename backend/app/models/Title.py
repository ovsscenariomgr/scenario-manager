from django.db import models
from django.core.validators import MinValueValidator
from .Header import Header

class Title(models.Model):
    header = models.OneToOneField(Header, on_delete=models.CASCADE)
    name = models.CharField(max_length=256)
    top = models.IntegerField(default=0, validators=[MinValueValidator(0)]) # Distance from top in pixels, should there be a max?
    left = models.IntegerField(default=0, validators=[MinValueValidator(0)]) # Distance from left in pixels, should there be a max?