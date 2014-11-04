from django import forms
from crispy_forms.helper import FormHelper, Layout
from crispy_forms.layout import Submit
from crispy_forms.bootstrap import InlineRadios

from .models import SignUp


class SignUpForm(forms.ModelForm):
    class Meta:
        model = SignUp

