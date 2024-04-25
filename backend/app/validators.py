import re
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError

def validate_html5_color(color):
    WEB_SAFE = ['aqua', 'black', 'blue', 'fuchsia', 'gray', 'green', 'lime', 'maroon', 'navy', 'olive', 'orange', 'purple', 'red', 'silver', 'teal', 'white', 'yellow']
    if not (re.match(r'^#[A-Z0-9]{6}', color) or color in WEB_SAFE):
        raise ValidationError(_('%s is not an HTML5 compatible specifier for color' % color))

def validate_left_lung_sound(sound):
    if sound == 'same_as_left':
        raise ValidationError(_('Cannot be assigned value: same_as_left'))

def validate_right_lung_sound(sound):
    if sound == 'same_as_right':
        raise ValidationError(_('Cannot be assigned value: same_as_right'))