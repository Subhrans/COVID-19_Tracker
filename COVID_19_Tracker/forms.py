from django import forms
from .models import India

class IndiaForm(forms.ModelForm):
    class Mata:
        model=India
        fields="__all__"