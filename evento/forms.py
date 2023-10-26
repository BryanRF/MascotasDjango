# forms.py

from django import forms
from api.models import Donacion, Evento, EventoParticipante, Premio, Ganador 

class DonacionForm(forms.ModelForm):
    class Meta:
        model = Donacion
        fields = ['descripcion', 'fecha_donacion', 'persona']

class EventoForm(forms.ModelForm):
    class Meta:
        model = Evento
        fields = ['nombre', 'fecha_inicio', 'fecha_fin_participacion', 'costo_participacion']

class EventoParticipanteForm(forms.ModelForm):
    class Meta:
        model = EventoParticipante
        fields = ['evento', 'participante']

class PremioForm(forms.ModelForm):
    class Meta:
        model = Premio
        fields = ['nombre', 'descripcion', 'evento']

class GanadorForm(forms.ModelForm):
    class Meta:
        model = Ganador
        fields = ['evento', 'premio', 'participante']
