from django.contrib import admin
import nested_admin

# Register your models here.
from .models import *

class TitleInline(nested_admin.NestedStackedInline):
    model = Title

class HeaderInline(nested_admin.NestedStackedInline):
    model = Header
    inlines = [TitleInline]

class AvatarInline(nested_admin.NestedStackedInline):
    model = Avatar

class SummaryInline(nested_admin.NestedStackedInline):
    model = Summary

class ControlInline(nested_admin.NestedStackedInline):
    model = Control

class ProfileInline(nested_admin.NestedStackedInline):
    model = Profile
    inlines = [AvatarInline, SummaryInline, ControlInline]

class ScenarioAdmin(nested_admin.NestedModelAdmin):
    model = Scenario
    inlines = [HeaderInline, ProfileInline]

admin.site.register(Scenario, ScenarioAdmin)