import nested_admin
from .forms import BaseNestedInlineForm
from app.models import (SceneInitRespiration, SceneInitGeneral, SceneInitCardiac, SceneInit,
    ParameterTriggerCardiac, ParameterTriggerGeneral, ParameterTriggerRespiration, Trigger,
    Timeout, Scene)


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
    # fk_name = 'scenefk'
    classes = ('grp-collapse grp-closed',)
    inline_classes = ('grp-collapse grp-closed',)

class SceneInline(nested_admin.NestedStackedInline):
    model = Scene
    extra = 1
    inlines = [TimeoutInline, TriggerInline]
    # inlines = [SceneInitInline, TimeoutInline, TriggerInline]
    classes = ('grp-collapse grp-closed',)
    inline_classes = ('grp-collapse grp-closed',)