import nested_admin
from .forms import BaseNestedInlineForm
from app.models import Title, Header
                     
class TitleInline(nested_admin.NestedStackedInline):
    model = Title
    form = BaseNestedInlineForm
    classes = ('grp-collapse grp-closed',) # Set so default is form closed, values can be grp-open or grp-closed.
    inline_classes = ('grp-collapse grp-closed',)

class HeaderInline(nested_admin.NestedStackedInline):
    model = Header
    inlines = [TitleInline,]
    classes = ('grp-collapse grp-closed',)
    inline_classes = ('grp-collapse grp-closed',)