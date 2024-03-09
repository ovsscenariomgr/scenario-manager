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
    classes = ('grp-collapse grp-closed',) # Set so default is form closed, values can be grp-open or grp-closed.
    inline_classes = ('grp-collapse grp-closed',)

class HeaderInline(nested_admin.NestedStackedInline):
    model = Header
    inlines = [TitleInline,]
    classes = ('grp-collapse grp-closed',)
    inline_classes = ('grp-collapse grp-closed',)

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

class VocalsInline(nested_admin.NestedStackedInline):
    model = VocalFile
    form = BaseNestedInlineForm
    fk_name = 'scenario'
    extra = 1
    classes = ('grp-collapse grp-closed',)
    inline_classes = ('grp-collapse grp-closed',)

class MediaInline(nested_admin.NestedStackedInline):
    model = MediaFile
    form = BaseNestedInlineForm
    fk_name = 'scenario'
    extra = 1
    classes = ('grp-collapse grp-closed',)
    inline_classes = ('grp-collapse grp-closed',)

class ScenarioInitRespirationInline(nested_admin.NestedStackedInline):
    model = ScenarioInitRespiration
    form = BaseNestedInlineForm
    fk_name = 'scenario_init'
    classes = ('grp-collapse grp-closed',)
    inline_classes = ('grp-collapse grp-closed',)

class ScenarioInitGeneralInline(nested_admin.NestedStackedInline):
    model = ScenarioInitGeneral
    form = BaseNestedInlineForm
    fk_name = 'scenario_init'
    classes = ('grp-collapse grp-closed',)
    inline_classes = ('grp-collapse grp-closed',)

class ScenarioInitCardiacInline(nested_admin.NestedStackedInline):
    model = ScenarioInitCardiac
    form = BaseNestedInlineForm
    fk_name = 'scenario_init'
    classes = ('grp-collapse grp-closed',)
    inline_classes = ('grp-collapse grp-closed',)

class ScenarioInitInline(nested_admin.NestedStackedInline):
    model = ScenarioInit
    inlines = [ScenarioInitCardiacInline, ScenarioInitRespirationInline, ScenarioInitGeneralInline,]
    classes = ('grp-collapse grp-closed',)
    inline_classes = ('grp-collapse grp-closed',)

class EventInline(nested_admin.NestedStackedInline):
    model = Event
    form = BaseNestedInlineForm
    extra = 1
    fk_name = 'category'
    classes = ('grp-collapse grp-closed',)
    inline_classes = ('grp-collapse grp-closed',)

class CategoryInline(nested_admin.NestedStackedInline):
    model = Category
    extra = 1
    inlines = [EventInline]
    classes = ('grp-collapse grp-closed',)
    inline_classes = ('grp-collapse grp-closed',)

class SceneInitRespirationInline(nested_admin.NestedStackedInline):
    model = SceneInitRespiration
    form = BaseNestedInlineForm
    fk_name = 'scene_init'
    classes = ('grp-collapse grp-closed',)
    inline_classes = ('grp-collapse grp-closed',)

class SceneInitGeneralInline(nested_admin.NestedStackedInline):
    model = SceneInitGeneral
    form = BaseNestedInlineForm
    fk_name = 'scene_init'
    classes = ('grp-collapse grp-closed',)
    inline_classes = ('grp-collapse grp-closed',)

class SceneInitCardiacInline(nested_admin.NestedStackedInline):
    model = SceneInitCardiac
    form = BaseNestedInlineForm
    fk_name = 'scene_init'
    classes = ('grp-collapse grp-closed',)
    inline_classes = ('grp-collapse grp-closed',)

class SceneInitInline(nested_admin.NestedStackedInline):
    model = SceneInit
    fk_name = 'scene'
    inlines = [SceneInitCardiacInline, SceneInitRespirationInline, SceneInitGeneralInline,]
    classes = ('grp-collapse grp-closed',)
    inline_classes = ('grp-collapse grp-closed',)

class TimeoutInline(nested_admin.NestedStackedInline):
    model = Timeout
    form = BaseNestedInlineForm
    fk_name = 'scenefk'
    classes = ('grp-collapse grp-closed',)
    inline_classes = ('grp-collapse grp-closed',)

class ParameterTriggerRespirationInline(nested_admin.NestedStackedInline):
    model = ParameterTriggerRespiration
    form = BaseNestedInlineForm
    fk_name = 'trigger'
    classes = ('grp-collapse grp-closed',)
    inline_classes = ('grp-collapse grp-closed',)

class ParameterTriggerGeneralInline(nested_admin.NestedStackedInline):
    model = ParameterTriggerGeneral
    form = BaseNestedInlineForm
    fk_name = 'trigger'
    classes = ('grp-collapse grp-closed',)
    inline_classes = ('grp-collapse grp-closed',)

class ParameterTriggerCardiacInline(nested_admin.NestedStackedInline):
    model = ParameterTriggerCardiac
    form = BaseNestedInlineForm
    fk_name = 'trigger'
    classes = ('grp-collapse grp-closed',)
    inline_classes = ('grp-collapse grp-closed',)

class TriggerInline(nested_admin.NestedStackedInline):
    model = Trigger
    inlines = [ParameterTriggerCardiacInline, ParameterTriggerRespirationInline, ParameterTriggerGeneralInline]
    extra = 1
    fk_name = 'scenefk'
    classes = ('grp-collapse grp-closed',)
    inline_classes = ('grp-collapse grp-closed',)

class SceneInline(nested_admin.NestedStackedInline):
    model = Scene
    extra = 1
    inlines = [SceneInitInline, TimeoutInline]
    # inlines = [SceneInitInline, TimeoutInline, TriggerInline]
    classes = ('grp-collapse grp-closed',)
    inline_classes = ('grp-collapse grp-closed',)

@admin.register(Scenario)
class ScenarioAdmin(nested_admin.NestedModelAdmin):
    model = Scenario
    inlines = [HeaderInline, ProfileInline, VocalsInline, MediaInline, ScenarioInitInline, CategoryInline, SceneInline]
    classes = ('grp-collapse grp-closed',)
    inline_classes = ('grp-collapse grp-closed',)