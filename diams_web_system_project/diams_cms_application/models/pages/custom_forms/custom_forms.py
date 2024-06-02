from django import forms
from wagtail.admin.forms import WagtailAdminPageForm


class CustomPageForm(WagtailAdminPageForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'slug' in self.fields:
            self.fields['slug'].widget = forms.HiddenInput()
