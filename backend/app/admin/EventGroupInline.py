import nested_admin
from .forms import BaseNestedInlineForm
from app.models import Event, EventGroup

class EventInline(nested_admin.NestedStackedInline):
    model = Event
    form = BaseNestedInlineForm
    extra = 1
    fk_name = 'eventgroup'
    classes = ('grp-collapse grp-closed',)
    inline_classes = ('grp-collapse grp-closed',)

class EventGroupInline(nested_admin.NestedStackedInline):
    model = EventGroup
    extra = 1
    inlines = [EventInline]
    classes = ('grp-collapse grp-closed',)
    inline_classes = ('grp-collapse grp-closed',)