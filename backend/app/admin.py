from django.contrib import admin
from nested_inline.admin import NestedStackedInline, NestedModelAdmin

# Register your models here.
from .models import Scenario, Header, Title

class TitleInline(NestedStackedInline):
    model = Title
    extra = 1
    fk_name = 'header'
class HeaderInline(NestedStackedInline):
    model = Header
    extra = 1
    fk_name = 'scenario'
    inlines = [TitleInline]

@admin.register(Scenario)
class ScenarioAdmin(NestedModelAdmin):
    model = Scenario
    inlines = [HeaderInline]