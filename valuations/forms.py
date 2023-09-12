from django import forms
from .models import Valuation


class ValuationForm(forms.ModelForm):
    class Meta:
        model = Valuation
        fields = ['nom', 'titol', 'valoracio']
