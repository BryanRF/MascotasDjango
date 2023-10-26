# forms.py

from django import forms
from api.models import Adopcion

class AdopcionForm(forms.ModelForm):
    class Meta:
        model = Adopcion
        fields = ['persona', 'mascota', 'fecha_adopcion', 'estado_adopcion', 'comentarios']
