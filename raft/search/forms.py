from django import forms

class SearchForm(forms.Form):
    term = forms.CharField(required=False, widget=forms.TextInput(
        attrs={
            'class': 'form-control', 
            'placeholder': "Enter a cuisine, food or keyword."
        }
    ))
    location = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': "Location",
            'value': 'SEATTLE, WA'
        }
    ))
    