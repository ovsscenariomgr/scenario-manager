import nested_admin
from .forms import BaseNestedInlineForm
from app.models import Avatar, Summary, Control, Profile


class AvatarInline(nested_admin.NestedStackedInline):
    model = Avatar
    form = BaseNestedInlineForm
    classes = ('grp-collapse grp-closed',)
    inline_classes = ('grp-collapse grp-closed',)

class SummaryInline(nested_admin.NestedStackedInline):
    model = Summary
    form = BaseNestedInlineForm
    classes = ('grp-collapse grp-closed',)
    inline_classes = ('grp-collapse grp-closed',)

class ControlInline(nested_admin.NestedStackedInline):
    model = Control
    form = BaseNestedInlineForm
    extra = 1
    classes = ('grp-collapse grp-closed',)
    inline_classes = ('grp-collapse grp-closed',)

class ProfileInline(nested_admin.NestedStackedInline):
    model = Profile
    inlines = [AvatarInline, SummaryInline, ControlInline,]
    classes = ('grp-collapse grp-closed',)
    inline_classes = ('grp-collapse grp-closed',)