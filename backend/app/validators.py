import re
from django.core.exceptions import ValidationError

def validate_html5_color(color):
    if not re.match(r'^#[A-Z0-9]{6}', color):
        raise ValidationError('%s is not an HTML5 compatible specifier for color' % color)