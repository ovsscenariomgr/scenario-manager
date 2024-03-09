from django.contrib import admin
import nested_admin
from .forms import BaseNestedInlineForm
from .models import (Title, Header, Avatar, Summary, Control, Profile,
    VocalFile, MediaFile, Scenario, ScenarioInit, ScenarioInitCardiac,
    ScenarioInitGeneral, ScenarioInitRespiration, Category, Event,
    Scene, SceneInit, SceneInitCardiac, SceneInitGeneral, SceneInitRespiration,
    Trigger, ParameterTriggerCardiac, ParameterTriggerGeneral, ParameterTriggerRespiration,
    Timeout)

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

class ScenarioInitRespirationInline(nested_admin.NestedStackedInline):
    model = ScenarioInitRespiration
    form = BaseNestedInlineForm
    fk_name = 'scenario_init'
    classes = ('grp-collapse grp-open',)
    inline_classes = ('grp-collapse grp-open',)

class ScenarioInitGeneralInline(nested_admin.NestedStackedInline):
    model = ScenarioInitGeneral
    form = BaseNestedInlineForm
    fk_name = 'scenario_init'
    classes = ('grp-collapse grp-open',)
    inline_classes = ('grp-collapse grp-open',)

class ScenarioInitCardiacInline(nested_admin.NestedStackedInline):
    model = ScenarioInitCardiac
    form = BaseNestedInlineForm
    fk_name = 'scenario_init'
    classes = ('grp-collapse grp-open',)
    inline_classes = ('grp-collapse grp-open',)

class ScenarioInitInline(nested_admin.NestedStackedInline):
    model = ScenarioInit
    inlines = [ScenarioInitCardiacInline, ScenarioInitRespirationInline, ScenarioInitGeneralInline,]
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

class SceneInitRespirationInline(nested_admin.NestedStackedInline):
    model = SceneInitRespiration
    form = BaseNestedInlineForm
    fk_name = 'scene_init'
    classes = ('grp-collapse grp-open',)
    inline_classes = ('grp-collapse grp-open',)

class SceneInitGeneralInline(nested_admin.NestedStackedInline):
    model = SceneInitGeneral
    form = BaseNestedInlineForm
    fk_name = 'scene_init'
    classes = ('grp-collapse grp-open',)
    inline_classes = ('grp-collapse grp-open',)

class SceneInitCardiacInline(nested_admin.NestedStackedInline):
    model = SceneInitCardiac
    form = BaseNestedInlineForm
    fk_name = 'scene_init'
    classes = ('grp-collapse grp-open',)
    inline_classes = ('grp-collapse grp-open',)

class SceneInitInline(nested_admin.NestedStackedInline):
    model = SceneInit
    fk_name = 'scene'
    inlines = [SceneInitCardiacInline, SceneInitRespirationInline, SceneInitGeneralInline,]
    classes = ('grp-collapse grp-open',)
    inline_classes = ('grp-collapse grp-open',)

class TimeoutInline(nested_admin.NestedStackedInline):
    model = Timeout
    form = BaseNestedInlineForm
    fk_name = 'scenefk'
    classes = ('grp-collapse grp-open',)
    inline_classes = ('grp-collapse grp-open',)

class ParameterTriggerRespirationInline(nested_admin.NestedStackedInline):
    model = ParameterTriggerRespiration
    form = BaseNestedInlineForm
    fk_name = 'trigger'
    classes = ('grp-collapse grp-open',)
    inline_classes = ('grp-collapse grp-open',)

class ParameterTriggerGeneralInline(nested_admin.NestedStackedInline):
    model = ParameterTriggerGeneral
    form = BaseNestedInlineForm
    fk_name = 'trigger'
    classes = ('grp-collapse grp-open',)
    inline_classes = ('grp-collapse grp-open',)

class ParameterTriggerCardiacInline(nested_admin.NestedStackedInline):
    model = ParameterTriggerCardiac
    form = BaseNestedInlineForm
    fk_name = 'trigger'
    classes = ('grp-collapse grp-open',)
    inline_classes = ('grp-collapse grp-open',)

class TriggerInline(nested_admin.NestedStackedInline):
    model = Trigger
    inlines = [ParameterTriggerCardiacInline, ParameterTriggerRespirationInline, ParameterTriggerGeneralInline]
    extra = 1
    fk_name = 'scenefk'
    classes = ('grp-collapse grp-open',)
    inline_classes = ('grp-collapse grp-open',)

class SceneInline(nested_admin.NestedStackedInline):
    model = Scene
    extra = 1
    inlines = [SceneInitInline, TimeoutInline]
    # inlines = [SceneInitInline, TimeoutInline, TriggerInline]
    classes = ('grp-collapse grp-open',)
    inline_classes = ('grp-collapse grp-open',)

@admin.register(Scenario)
class ScenarioAdmin(nested_admin.NestedModelAdmin):
    model = Scenario
    inlines = [HeaderInline, ProfileInline, VocalsInline, MediaInline, ScenarioInitInline, CategoryInline, SceneInline]
    classes = ('grp-collapse grp-open',)
    inline_classes = ('grp-collapse grp-open',)