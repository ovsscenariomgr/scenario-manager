from django.contrib import admin
import nested_admin
from .forms import TitleForm, AvatarForm, SummaryForm, ControlForm
from .models import *

class TitleInline(nested_admin.NestedStackedInline):
    model = Title
    form = TitleForm
    classes = ('grp-collapse grp-open',) # Set so default is form opened.
    inline_classes = ('grp-collapse grp-open',)

class HeaderInline(nested_admin.NestedStackedInline):
    model = Header
    inlines = [TitleInline,]
    classes = ('grp-collapse grp-open',)
    inline_classes = ('grp-collapse grp-open',)

class AvatarInline(nested_admin.NestedStackedInline):
    model = Avatar
    form = AvatarForm
    classes = ('grp-collapse grp-open',)
    inline_classes = ('grp-collapse grp-open',)

class SummaryInline(nested_admin.NestedStackedInline):
    model = Summary
    form = SummaryForm
    classes = ('grp-collapse grp-open',)
    inline_classes = ('grp-collapse grp-open',)

class ControlInline(nested_admin.NestedStackedInline):
    model = Control
    form = ControlForm
    extra = 1
    classes = ('grp-collapse grp-open',)
    inline_classes = ('grp-collapse grp-open',)

class ProfileInline(nested_admin.NestedStackedInline):
    model = Profile
    inlines = [AvatarInline, SummaryInline, ControlInline,]
    classes = ('grp-collapse grp-open',)
    inline_classes = ('grp-collapse grp-open',)

@admin.register(Scenario)
class ScenarioAdmin(nested_admin.NestedModelAdmin):
    model = Scenario
    inlines = [HeaderInline, ProfileInline,]
    classes = ('grp-collapse grp-open',)
    inline_classes = ('grp-collapse grp-open',)