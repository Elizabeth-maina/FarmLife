from django.forms import ModelForm
from django import forms
from .models import *


class FarmersForm(ModelForm):
    class Meta:
        model = Farmer
        fields = '__all__'
