from django.contrib import admin
import nested_admin
from .forms import BaseNestedInlineForm
from .models import (Title, Header, Avatar, Summary, Control, Profile,
    VocalFile, MediaFile, Scenario, Init, InitCardiac,
    InitGeneral, InitRespiration, Category, Event)

class TitleInline(nested_admin.NestedStackedInline):
    model = Title
    form = BaseNestedInlineForm
    classes = ('grp-collapse grp-open',) # Set so default is form opened.
    inline_classes = ('grp-collapse grp-open',)

class HeaderInline(nested_admin.NestedStackedInline):
    model = Header
    inlines = [TitleInline,]
    classes = ('grp-collapse grp-open',)
    inline_classes = ('grp-collapse grp-open',)

class AvatarInline(nested_admin.NestedStackedInline):
    model = Avatar
    form = BaseNestedInlineForm
    classes = ('grp-collapse grp-open',)
    inline_classes = ('grp-collapse grp-open',)

class SummaryInline(nested_admin.NestedStackedInline):
    model = Summary
    form = BaseNestedInlineForm
    classes = ('grp-collapse grp-open',)
    inline_classes = ('grp-collapse grp-open',)

class ControlInline(nested_admin.NestedStackedInline):
    model = Control
    form = BaseNestedInlineForm
    extra = 1
    classes = ('grp-collapse grp-open',)
    inline_classes = ('grp-collapse grp-open',)

class ProfileInline(nested_admin.NestedStackedInline):
    model = Profile
    inlines = [AvatarInline, SummaryInline, ControlInline,]
    classes = ('grp-collapse grp-open',)
    inline_classes = ('grp-collapse grp-open',)

class VocalsInline(nested_admin.NestedStackedInline):
    model = VocalFile
    form = BaseNestedInlineForm
    fk_name = 'scenario'
    extra = 1
    classes = ('grp-collapse grp-open',)
    inline_classes = ('grp-collapse grp-open',)

class MediaInline(nested_admin.NestedStackedInline):
    model = MediaFile
    form = BaseNestedInlineForm
    fk_name = 'scenario'
    extra = 1
    classes = ('grp-collapse grp-open',)
    inline_classes = ('grp-collapse grp-open',)

class InitRespirationInline(nested_admin.NestedStackedInline):
    model = InitRespiration
    form = BaseNestedInlineForm
    fk_name = 'init'
    classes = ('grp-collapse grp-open',) # Set so default is form opened.
    inline_classes = ('grp-collapse grp-open',)

class InitGeneralInline(nested_admin.NestedStackedInline):
    model = InitGeneral
    form = BaseNestedInlineForm
    fk_name = 'init'
    classes = ('grp-collapse grp-open',) # Set so default is form opened.
    inline_classes = ('grp-collapse grp-open',)

class InitCardiacInline(nested_admin.NestedStackedInline):
    model = InitCardiac
    form = BaseNestedInlineForm
    fk_name = 'init'
    classes = ('grp-collapse grp-open',) # Set so default is form opened.
    inline_classes = ('grp-collapse grp-open',)

class InitInline(nested_admin.NestedStackedInline):
    model = Init
    inlines = [InitCardiacInline, InitRespirationInline, InitGeneralInline,]
    classes = ('grp-collapse grp-open',)
    inline_classes = ('grp-collapse grp-open',)

class EventInline(nested_admin.NestedStackedInline):
    model = Event
    form = BaseNestedInlineForm
    extra = 1
    fk_name = 'category'
    classes = ('grp-collapse grp-open',)
    inline_classes = ('grp-collapse grp-open',)

class CategoryInline(nested_admin.NestedStackedInline):
    model = Category
    extra = 1
    inlines = [EventInline]
    classes = ('grp-collapse grp-open',)
    inline_classes = ('grp-collapse grp-open',)

@admin.register(Scenario)
class ScenarioAdmin(nested_admin.NestedModelAdmin):
    model = Scenario
    inlines = [HeaderInline, ProfileInline, VocalsInline, MediaInline, InitInline, CategoryInline]
    classes = ('grp-collapse grp-open',)
    inline_classes = ('grp-collapse grp-open',)