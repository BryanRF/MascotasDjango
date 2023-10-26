# from django.views import View
from django.shortcuts import render
from django.http import JsonResponse
from django.views.generic import ListView
from api.models import Mascota,Especie,Evento
from datetime import date
from django.shortcuts import render, get_object_or_404
from uuid import UUID

class InicioView(ListView):
    model = Mascota
    template_name = 'inicio.html'
    context_object_name = 'mascotas'
    paginate_by = 8    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Obtener las especies con al menos una mascota registrada
        especies_con_mascotas = Especie.objects.filter(mascota__isnull=False).distinct()
        context['especies'] = especies_con_mascotas
        # Filtrar solo 6 mascotas por especie
        # context['mascotas'] = Mascota.objects.all()
        context['eventos'] = Evento.objects.filter(fecha_inicio__gte=date.today())
        context['mascotas_populares'] = Mascota.objects.order_by('-likes')[:4]
        return context
class EventoView:
    @staticmethod
    def ver_evento(request, evento_id):
        evento = Evento.objects.get(id=evento_id)
        return render(request, 'eventos.html', {'evento': evento})
