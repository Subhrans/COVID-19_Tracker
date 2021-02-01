from django import forms
from .models import India


class IndiaForm(forms.ModelForm):
    class Mata:
        model = India
        fields = "__all__"



class SearchLocation(forms.Form):
    location_name = forms.CharField(max_length=1000,
                                    widget=forms.TextInput(attrs={'class': 'form-control bg-light border-0 search sm-search',
                                                                  'data-toggle': 'popover',
                                                                  'title': '',
                                                                  'data-content': "Default Value",
                                                                  # 'data-trigger':'focus',
                                                                  'data-placement': 'bottom',
                                                                  'data-html': "true",
                                                                  'placeholer':'type Country name',
                                                                  }))
