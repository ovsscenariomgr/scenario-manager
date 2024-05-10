from django.db import models
from .Scenario import Scenario
from ..validators import validate_html5_color

class Profile(models.Model):
    # This is placed in the <controls></controls> list in OvsXMLRenderer
    color = models.CharField(max_length=7, default='#000000', validators=[validate_html5_color])
    # avatar = OneToOneField(Avatar)
    # summary = OneToOneField(Summary)
    # controls = ForeignKey(Control)
    # Foreign Key
    scenario = models.OneToOneField(Scenario, on_delete=models.CASCADE)