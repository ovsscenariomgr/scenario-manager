from django.db import models
from django.core.validators import MinValueValidator
from .Header import Header

class Title(models.Model):
    name = models.CharField(max_length=256, default='Titular Title')
    top = models.IntegerField(default=5, validators=[MinValueValidator(0)]) # Distance from top in pixels, should there be a max?
    left = models.IntegerField(default=10, validators=[MinValueValidator(0)]) # Distance from left in pixels, should there be a max?
    # Foreign Key
    header = models.OneToOneField(Header, on_delete=models.CASCADE)