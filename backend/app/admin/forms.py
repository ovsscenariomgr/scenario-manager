# Overriding has_changed in nested models so NestedInline will save if the defaults have not changed.
from django import forms

class BaseNestedInlineForm(forms.ModelForm):
    def has_changed(self):
        return not self.instance.pk or super().has_changed()