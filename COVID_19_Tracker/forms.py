from django import forms
from .models import India,Countries
country_name=Countries.objects.values_list('country',flat=True)
class IndiaForm(forms.ModelForm):
    class Mata:
        model=India
        fields="__all__"


class SearchLocation(forms.Form):
    location_name=forms.CharField(max_length=1000,widget=forms.TextInput(attrs={'class':'form-control bg-light border-0 search',
                                                                                'data-toggle':'popover',
                                                                                'title':'',
                                                                                'data-content':"hello",
                                                                                # 'data-trigger':'focus',
                                                                                'data-placement':'bottom',
                                                                                'data-html':"true",
                                                                                }))