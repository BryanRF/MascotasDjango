from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core import serializers
from datetime import datetime
from .forms import MascotaForm,AdopcionForm
from api.models import Evento ,Mascota,Especie,Adopcion,EstadoAdopcion,Persona
from django.http import JsonResponse
from datetime import date
import json
def listado(request):
	lista = serializers.serialize('json', Mascota.objects.all().order_by('id'))
	return HttpResponse(lista, content_type='application/json')


def index(request):
    # Obtén todas las mascotas que no tienen una adopción en estado "Aprobado"
    mascotas = Mascota.objects.exclude(adopcion__estado_adopcion__estado='Aprobado').order_by('id')
    contexto = {'mascotas': mascotas}
    return render(request, 'adopcion.html', contexto)



def mascota_view(request):
    if request.method=='POST':
        form = MascotaForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('mascota_listar')
    else:
        form = MascotaForm()
    return render(request,'mascotas.html',{'form':form})

def mascota_usuario_list(request,id_usuario):
    persona = Persona.objects.get(user__id=id_usuario)
    adopciones_aprobadas = Adopcion.objects.filter(usuario_adoptante=persona, estado_adopcion__estado='Aprobado')
    mascotas_aprobadas = [adopcion.mascota for adopcion in adopciones_aprobadas]
    contexto = {'mascotas_aprobadas': mascotas_aprobadas}
    return render(request, 'mascotas_aprobadas.html', contexto)

from django.http import JsonResponse

def mascota_datatables_list(request, id_usuario):
    persona = Persona.objects.get(user__id=id_usuario)
    adopciones_aprobadas = Adopcion.objects.filter(usuario_adoptante=persona, estado_adopcion__estado='Aprobado')
    mascotas_aprobadas = [adopcion.mascota for adopcion in adopciones_aprobadas]

    data = []
    for mascota in mascotas_aprobadas:
        data.append({
            'codigo': mascota.codigo,
            'imagen': mascota.imagen_set.first().imagen.url,
            'nombre': mascota.nombre,
            'especie': mascota.especie.nombre,
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




def mascota_list(request):
    mascotas = Mascota.objects.all().order_by('id').values()
    return JsonResponse({'mascotas': list(mascotas)})

def mascota_id_list(request, id_mascota):
    mascota = Mascota.objects.values().get(id=id_mascota)
    return JsonResponse( mascota)

def mascota_like(request, id_mascota):
    mascota = Mascota.objects.get(id=id_mascota)
    mascota.like()
    return JsonResponse({'success': True, 'message': '¡Like agregado correctamente!', 'likes': mascota.likes})




