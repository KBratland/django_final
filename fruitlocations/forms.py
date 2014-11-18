__author__ = 'student'
from django import forms


class AddFruit(forms.Form):

    coordinates = forms.CharField(max_length=200, required=True)
    fruit_variety = forms.CharField(max_length=100, required=True)

    def clean(self):
        cleaned_data = self.cleaned_data

        coordinates = cleaned_data.get("coordinates")
        fruit_variety = cleaned_data.get("owner")

        return cleaned_data

    class Meta:
        model = AddFruit
