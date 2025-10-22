from django import forms
from .models import Sucursal

class SucursalForm(forms.ModelForm):
    class Meta:
        model = Sucursal
        fields = ['nombre_cine', 'direccion', 'ciudad', 'telefono', 'numero_salas', 'imagen_sucursal']