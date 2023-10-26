from rest_framework import serializers
from ..models import Evento

class EventoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evento
        fields = ['nombre', 'fecha_inicio', 'fecha_fin_participacion', 'costo_participacion']
