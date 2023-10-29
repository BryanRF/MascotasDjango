# forms.py

from django import forms
from api.models import Adopcion

class AdopcionForm(forms.ModelForm):
    class Meta:
        model = Adopcion
        fields = ['usuario_adoptante', 'mascota', 'fecha_adopcion', 'fecha_visita', 'estado_adopcion', 'comentarios']
