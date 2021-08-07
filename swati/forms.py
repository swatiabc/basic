from django import forms
from django.forms import fields
from . import models

class DestinationForm(forms.ModelForm):
    class Meta:
        model = models.Destination
        fields = "__all__"