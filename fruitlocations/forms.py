__author__ = 'student'
from django.contrib.gis import admin
from django import forms
from models import FruitLocations


class AddFruit(forms.Form):

    coordinates = forms.CharField(max_length=200, required=True)
    fruit_variety = forms.CharField(max_length=50, required=True)

    def clean(self):
        cleaned_data = self.cleaned_data

        coordinates = cleaned_data.get("coordinates")
        fruit_variety = cleaned_data.get("fruit_variety")

        return cleaned_data

    class Meta:
        model = FruitLocations
