# Overriding has_changed in nested models so NestedInline will save if the defaults have not changed.
from django import forms

class BaseNestedInlineForm(forms.ModelForm):
    def has_changed(self):
        return not self.instance.pk or super().has_changed()

class AvatarForm(BaseNestedInlineForm):
    pass

class ControlForm(BaseNestedInlineForm):
    pass

class FileForm(BaseNestedInlineForm):
    pass

class InitCardiacForm(BaseNestedInlineForm):
    pass

class InitGeneralForm(BaseNestedInlineForm):
    pass

class InitRespirationForm(BaseNestedInlineForm):
    pass

class SummaryForm(BaseNestedInlineForm):
    pass

class TitleForm(BaseNestedInlineForm):
    pass