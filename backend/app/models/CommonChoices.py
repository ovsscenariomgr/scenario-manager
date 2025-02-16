from django.db import models

class OnOffChoices(models.IntegerChoices):
    OFF = 0
    ON = 1