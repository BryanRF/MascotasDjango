# proyecto/src/views/eventos_view.py

from django.shortcuts import render
from api.models import Evento

def ver_evento(request, evento_id):
    evento = Evento.objects.get(id=evento_id)
    return render(request, 'eventos.html', {'evento': evento})
