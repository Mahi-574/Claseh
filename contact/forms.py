from django.core.exceptions import ValidationError
from django.forms import ModelForm, Field, TextInput
from django import forms
from .models import Contact
from django.utils.translation import gettext_lazy as _


class ContactForm(ModelForm):

    class Meta:
        model = Contact
        fields = '__all__'

        def clean(self):
            cleaned_data = super().clean()
            name = self.cleaned_data['name']
            if (name == "") | (name == None):
                raise forms.ValidationError('لطفا فیلد نام را پر نمایید!')

        help_texts = {
            "name": _("Some useful help text."),
        }
        error_messages = {
            "name": {
                "required": _("This writer's name is too long."),
            },
        }









