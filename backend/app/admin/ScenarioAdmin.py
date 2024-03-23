from django.contrib import admin
import nested_admin
from app.models import Scenario
from .HeaderInline import HeaderInline
from .ProfileInline import ProfileInline
from .VocalsInline import VocalsInline
from .MediaInline import MediaInline
from .ScenarioInitInline import ScenarioInitInline
from .CategoryInline import CategoryInline
from .SceneInline import SceneInline

@admin.register(Scenario)
class ScenarioAdmin(nested_admin.NestedModelAdmin):
    model = Scenario
    inlines = [HeaderInline, ProfileInline, VocalsInline, MediaInline, ScenarioInitInline, CategoryInline, SceneInline]
    classes = ('grp-collapse grp-closed',)
    inline_classes = ('grp-collapse grp-closed',)