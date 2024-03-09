import nested_admin
from .forms import BaseNestedInlineForm
from app.models import ParameterTriggerCardiac, ParameterTriggerGeneral, ParameterTriggerRespiration, Trigger

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