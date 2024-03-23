import nested_admin
from .forms import BaseNestedInlineForm
from .SceneInitInline import SceneInitInline
from .TriggerInline import TriggerInline
from app.models import Timeout, Scene

class TimeoutInline(nested_admin.NestedStackedInline):
    model = Timeout
    form = BaseNestedInlineForm
    fk_name = 'scenefk'
    classes = ('grp-collapse grp-closed',)
    inline_classes = ('grp-collapse grp-closed',)

class SceneInline(nested_admin.NestedStackedInline):
    model = Scene
    extra = 1
    inlines = [SceneInitInline, TimeoutInline, TriggerInline]
    classes = ('grp-collapse grp-closed',)
    inline_classes = ('grp-collapse grp-closed',)