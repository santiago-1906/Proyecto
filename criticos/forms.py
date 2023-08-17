from django import forms
from .models import Restaurante, Critico


class RestauranteForm(forms.ModelForm):
    class Meta:
        model = Restaurante
        fields = ['nombre', 'direccion', 'telefono', 'descripcion']

class CriticoForm(forms.ModelForm):
    class Meta:
        model = Critico
        fields = ['nombre', 'email', 'telefono', 'bio']