from django import forms
from .models import PriceProd

class PriceProdForm(forms.ModelForm):
    class Meta:
        model = PriceProd
        fields = ['priceprod', 'dateverify']  # Campos que o usuário pode editar
        widgets = {
            'dateverify': forms.DateInput(attrs={'type': 'date'}),
        }
