from django import forms
from .models import PriceProd
from .models import Product

class PriceProdForm(forms.ModelForm):
    class Meta:
        model = PriceProd
        fields = ['priceprod', 'dateverify']  # Campos que o usuário pode editar
        widgets = {
            'dateverify': forms.DateInput(attrs={'type': 'date'}),
        }



class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['nameprod', 'descprod'] 
