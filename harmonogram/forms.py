from django import forms

from .models import WywozSmieci


class WywozForm(forms.ModelForm):
    class Meta:
        model = WywozSmieci
        fields = ['data', 'typ_odpadu']
        widgets = {
            'data': forms.DateInput(attrs={'type': 'date', 'class': 'form-input'}),
            'typ_odpadu': forms.Select(attrs={'class': 'form-input'}),
        }
        labels = {
            'data': 'Data wywozu',
            'typ_odpadu': 'Typ odpadu',
        }
