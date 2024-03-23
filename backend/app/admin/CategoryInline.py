import nested_admin
from .forms import BaseNestedInlineForm
from app.models import Event, Category

class EventInline(nested_admin.NestedStackedInline):
    model = Event
    form = BaseNestedInlineForm
    extra = 1
    fk_name = 'category'
    classes = ('grp-collapse grp-closed',)
    inline_classes = ('grp-collapse grp-closed',)

class CategoryInline(nested_admin.NestedStackedInline):
    model = Category
    extra = 1
    inlines = [EventInline]
    classes = ('grp-collapse grp-closed',)
    inline_classes = ('grp-collapse grp-closed',)