# from django.views import View
from django.shortcuts import render
from django.http import JsonResponse
from django.views.generic import ListView
from api.models import Mascota,Especie




class InicioView(ListView):
    model = Mascota
    template_name = 'index.html'
    context_object_name = 'mascotas'
    paginate_by = 6    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Obtener las especies con al menos una mascota registrada
        especies_con_mascotas = Especie.objects.filter(mascota__isnull=False).distinct()
        context['especies'] = especies_con_mascotas
        # Filtrar solo 6 mascotas por especie
        context['mascotas'] = Mascota.objects.all()
        return context
    
class MascotasView(ListView):
    model = Mascota
    template_name = 'mascotas.html'
    context_object_name = 'mascotas'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Obtener las especies con al menos una mascota registrada
        especies_con_mascotas = Especie.objects.filter(mascota__isnull=False).distinct()
        context['especies'] = especies_con_mascotas
        # Filtrar solo 6 mascotas por especie
        context['mascotas'] = Mascota.objects.all()
        return context

class MascotasDataTablesView(ListView):
    def mascotas_datatables(self, request, *args, **kwargs):
        mascotas = Mascota.objects.all()
        data = []

        for mascota in mascotas:
            data.append({
                'nombre': mascota.nombre,
                'edad': mascota.edad,
                'descripcion': mascota.descripcion,
                'disponible': mascota.disponible,
                'color': mascota.color,
                'tamano': mascota.tamano,
                'genero': mascota.genero,
                'likes': mascota.likes,
                'id': mascota.id
            })

        return JsonResponse(data, safe=False)


def page_not_found(request):
    return render(request, 'index.html')