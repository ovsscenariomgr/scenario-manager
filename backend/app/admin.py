from django.contrib import admin
from nested_inline.admin import NestedStackedInline, NestedModelAdmin

# Register your models here.
from .models import *

class TitleInline(NestedStackedInline):
    model = Title
    extra = 1
    fk_name = 'header'
class HeaderInline(NestedStackedInline):
    model = Header
    extra = 1
    fk_name = 'scenario'
    inlines = [TitleInline]

class AvatarInline(NestedStackedInline):
    model = Avatar
    extra = 1
    fk_name = 'profile'

class SummaryInline(NestedStackedInline):
    model = Summary
    extra = 1
    fk_name = 'profile'

class ControlInline(NestedStackedInline):
    model = Control
    extra = 1
    fk_name = 'profile'

class ProfileInline(NestedStackedInline):
    model = Profile
    extra = 1
    fk_name = 'scenario'
    inlines = [AvatarInline, SummaryInline, ControlInline]

@admin.register(Scenario)
class ScenarioAdmin(NestedModelAdmin):
    model = Scenario
    inlines = [HeaderInline, ProfileInline]