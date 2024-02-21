from django.contrib import admin
from nested_inline.admin import NestedStackedInline, NestedModelAdmin

# Register your models here.
from .models import *

class TitleInline(NestedStackedInline):
    model = Title
    fk_name = 'header'

class HeaderInline(NestedStackedInline):
    model = Header
    fk_name = 'scenario'
    inlines = [TitleInline]

class AvatarInline(NestedStackedInline):
    model = Avatar
    fk_name = 'profile'

class SummaryInline(NestedStackedInline):
    model = Summary
    fk_name = 'profile'

class ControlInline(NestedStackedInline):
    model = Control
    extra = 2
    fk_name = 'profile'

class ProfileInline(NestedStackedInline):
    model = Profile
    fk_name = 'scenario'
    inlines = [AvatarInline, SummaryInline, ControlInline]

@admin.register(Scenario)
class ScenarioAdmin(NestedModelAdmin):
    model = Scenario
    inlines = [HeaderInline, ProfileInline]

admin.site.register(Profile)
admin.site.register(Control)
admin.site.register(Avatar)
admin.site.register(Summary)
admin.site.register(Header)
admin.site.register(Title)