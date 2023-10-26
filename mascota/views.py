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

def mascota_list(request):
    mascota = Mascota.objects.all().order_by('id')
    contexto = {'mascotas':mascota}
    return render(request,'mascotas.html',contexto)

def mascota_view(request):
    if request.method == 'POST':
        form = MascotaForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({'success': True, 'message': 'Mascota creada exitosamente'})
        else:
            return JsonResponse({'success': False, 'errors': form.errors})
    else:
        form = MascotaForm()
        return JsonResponse({'success': False, 'message': 'Método no permitido'})

def mascota_list(request):
    mascotas = Mascota.objects.all().order_by('id').values()
    return JsonResponse({'mascotas': list(mascotas)})

def mascota_edit(request, id_mascota):
    mascota = Mascota.objects.get(id=id_mascota)
    if request.method == 'GET':
        form = MascotaForm(instance=mascota)
        return JsonResponse({'success': False, 'message': 'Método no permitido'})
    else:
        form = MascotaForm(request.POST, instance=mascota)
        if form.is_valid():
            form.save()
            return JsonResponse({'success': True, 'message': 'Mascota actualizada exitosamente'})
        else:
            return JsonResponse({'success': False, 'errors': form.errors})

def mascota_delete(request, id_mascota):
    mascota = Mascota.objects.get(id=id_mascota)
    if request.method == 'POST':
        mascota.delete()
        return JsonResponse({'success': True, 'message': 'Mascota eliminada exitosamente'})
    else:
        return JsonResponse({'success': False, 'message': 'Método no permitido'})

def mascota_like(request, id_mascota):
    mascota = Mascota.objects.get(id=id_mascota)
    mascota.like()
    return JsonResponse({'success': True, 'message': '¡Like agregado correctamente!', 'likes': mascota.likes})


def adopcion_create(request):
    if request.method == 'POST':
        form = AdopcionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('adopcion_list')
    else:
        form = AdopcionForm()
    return render(request, 'adopcion/adopcion_form.html', {'form': form})
def adopcion_list(request):
    adopciones = Adopcion.objects.all()
    return render(request, 'adopcion/adopcion_list.html', {'adopciones': adopciones})
def adopcion_detail(request, id_adopcion):
    adopcion = Adopcion.objects.get(id=id_adopcion)
    return render(request, 'adopcion/adopcion_detail.html', {'adopcion': adopcion})
def adopcion_update(request, id_adopcion):
    adopcion = Adopcion.objects.get(id=id_adopcion)
    if request.method == 'POST':
        form = AdopcionForm(request.POST, instance=adopcion)
        if form.is_valid():
            form.save()
            return redirect('adopcion_list')
    else:
        form = AdopcionForm(instance=adopcion)
    return render(request, 'adopcion/adopcion_form.html', {'form': form})
def adopcion_delete(request, id_adopcion):
    adopcion = Adopcion.objects.get(id=id_adopcion)
    if request.method == 'POST':
        adopcion.delete()
        return redirect('adopcion_list')
    return render(request, 'adopcion/adopcion_confirm_delete.html', {'adopcion': adopcion})

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

    # Crear la nueva solicitud de adopción
    estado_pendiente = EstadoAdopcion.objects.get(estado='Pendiente')
    Adopcion.objects.create(
        usuario_adoptante_id=persona.id,
        mascota_id=id_mascota,
        estado_adopcion=estado_pendiente,
        comentarios=comentarios
    )

    return JsonResponse({'message': 'Enviado'}, status=200)
