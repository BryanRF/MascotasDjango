# views.py

from django.shortcuts import render, redirect
from .forms import AdopcionForm
from api.models import Adopcion,Persona
from django.http import JsonResponse


def adopciones_usuario_list(request,id_usuario):
    persona = Persona.objects.get(user__id=id_usuario)
    adopciones_aprobadas = Adopcion.objects.filter(usuario_adoptante=persona, estado_adopcion__estado='Aprobado')
    mascotas_aprobadas = [adopcion.mascota for adopcion in adopciones_aprobadas]
    contexto = {'mascotas_aprobadas': mascotas_aprobadas}
    return render(request, 'lista_solicitudes.html', contexto)


def adopciones_info(request, id_usuario):
    persona = Persona.objects.get(user__id=id_usuario)
    adopciones = Adopcion.objects.filter(usuario_adoptante=persona)

    data = []
    for adopcion in adopciones:
        data.append({
            'codigo': adopcion.mascota.codigo,
            'nombre': adopcion.mascota.nombre,
            'edad': adopcion.mascota.edad,
            'descripcion': adopcion.mascota.descripcion,
            'color': adopcion.mascota.color,
            'imagen': adopcion.mascota.imagen_set.first().imagen.url,
            'especie': adopcion.mascota.especie.nombre,
            'adopcion_estado': adopcion.estado_adopcion.estado,
        })

    return JsonResponse(data, safe=False)