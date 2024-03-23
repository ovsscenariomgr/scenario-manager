import nested_admin
from .forms import BaseNestedInlineForm
from app.models import VocalFile

class VocalsInline(nested_admin.NestedStackedInline):
    model = VocalFile
    form = BaseNestedInlineForm
    fk_name = 'scenario'
    extra = 1
    classes = ('grp-collapse grp-closed',)
    inline_classes = ('grp-collapse grp-closed',)