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
    mascota = Mascota.objects.all().order_by('id')
    contexto = {'mascotas':mascota}
    return render(request,'adopcion.html',contexto)


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



def proceso_adopcion(request):
    data = json.loads(request.body)
    # Obtener datos de la solicitud (id_usuario, mascota, comentarios)
    id_usuario = data.get('id_usuario')
    id_mascota = data.get('mascota')
    comentarios = data.get('comentarios')
    persona = Persona.objects.get(user__id=id_usuario)

    # Verificar si ya hay una solicitud pendiente para esta mascota y usuario
    if Adopcion.objects.filter(usuario_adoptante_id=persona.id, mascota_id=id_mascota, estado_adopcion__estado='Pendiente').exists():
        return JsonResponse({'message': 'Ya tienes una solicitud pendiente para esta mascota'}, status=400)

    # Verificar si la mascota ya tiene una adopción aprobada
    if Adopcion.objects.filter(mascota_id=id_mascota, estado_adopcion__estado='Aprobada').exists():
        return JsonResponse({'message': 'Esta mascota ya ha sido adoptada por otra persona'}, status=400)

    # Crear la nueva solicitud de adopción
    estado_pendiente = EstadoAdopcion.objects.get(estado='Pendiente')
    Adopcion.objects.create(
        usuario_adoptante_id=persona.id,
        mascota_id=id_mascota,
        estado_adopcion=estado_pendiente,
        comentarios=comentarios
    )

    return JsonResponse({'message': 'Enviado'}, status=200)

