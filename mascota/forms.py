from django import forms
from api.models import Mascota,Adopcion

class MascotaForm(forms.ModelForm):
    class Meta:
        model = Mascota
        fields = ['nombre', 'especie', 'edad', 'descripcion', 'disponible', 'color', 'tamano', 'etiquetas', 'genero']

class AdopcionForm(forms.ModelForm):
    class Meta:
        model = Adopcion
        fields = ['usuario_adoptante', 'mascota', 'fecha_adopcion', 'estado_adopcion', 'comentarios']
