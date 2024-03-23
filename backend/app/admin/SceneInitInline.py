import nested_admin
from .forms import BaseNestedInlineForm
from app.models import SceneInitRespiration, SceneInitGeneral, SceneInitCardiac, SceneInit

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