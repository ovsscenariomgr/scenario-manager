import nested_admin
from .forms import BaseNestedInlineForm
from app.models import MediaFile

class MediaInline(nested_admin.NestedStackedInline):
    model = MediaFile
    form = BaseNestedInlineForm
    fk_name = 'scenario'
    extra = 1
    classes = ('grp-collapse grp-closed',)
    inline_classes = ('grp-collapse grp-closed',)