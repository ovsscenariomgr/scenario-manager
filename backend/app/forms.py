# Overriding has_changed in nested models so NestedInline will save if the defaults have not changed.

from django import forms

class TitleForm(forms.ModelForm):
    def has_changed(self):
        return not self.instance.pk or super().has_changed()
   
class AvatarForm(forms.ModelForm):
    def has_changed(self):
        return not self.instance.pk or super().has_changed()
    
class SummaryForm(forms.ModelForm):
    def has_changed(self):
        return not self.instance.pk or super().has_changed()

class ControlForm(forms.ModelForm):
    def has_changed(self):
        return not self.instance.pk or super().has_changed()