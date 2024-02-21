import re
from django.core.exceptions import ValidationError

def validate_html5_color(color):
    WEB_SAFE = ['aqua', 'black', 'blue', 'fuchsia', 'gray', 'green', 'lime', 'maroon', 'navy', 'olive', 'orange', 'purple', 'red', 'silver', 'teal', 'white', 'yellow']
    if not re.match(r'^#[A-Z0-9]{6}', color) or color in WEB_SAFE:
        raise ValidationError('%s is not an HTML5 compatible specifier for color' % color)