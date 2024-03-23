import nested_admin
from .forms import BaseNestedInlineForm
from app.models import ScenarioInitRespiration, ScenarioInitGeneral, ScenarioInitCardiac, ScenarioInit

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