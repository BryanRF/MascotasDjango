# views.py

from django.shortcuts import render, redirect
from .forms import AdopcionForm
from api.models import Adopcion, Persona,EstadoAdopcion
from django.http import JsonResponse
import json

def adopciones_usuario_list(request, id_usuario):
    persona = Persona.objects.get(user__id=id_usuario)
    adopciones_aprobadas = Adopcion.objects.filter(
        usuario_adoptante=persona, estado_adopcion__estado='Aprobado')
    mascotas_aprobadas = [
        adopcion.mascota for adopcion in adopciones_aprobadas]
    contexto = {'mascotas_aprobadas': mascotas_aprobadas}
    return render(request, 'lista_solicitudes.html', contexto)


def adopciones_info(request, id_usuario):
    persona = Persona.objects.get(user__id=id_usuario)
    adopciones = Adopcion.objects.filter(usuario_adoptante=persona)

    data = []
    for adopcion in adopciones:
        data.append({
            'solicitud_id': adopcion.id,
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


def adopciones_eliminar(request, id_adopcion):
    if request.method == 'DELETE':
        try:
            adopcion = Adopcion.objects.get(id=id_adopcion)

            if adopcion.estado_adopcion.estado == 'Aprobado':
                return JsonResponse({'mensaje': 'No se puede eliminar una adopción aprobada'}, status=400)

            adopcion.delete()
            return JsonResponse({'mensaje': 'Adopción eliminada correctamente'}, status=200)
        except Adopcion.DoesNotExist:
            return JsonResponse({'mensaje': 'La adopción no existe'}, status=404)
        except Exception as e:
            return JsonResponse({'mensaje': str(e)}, status=500)
    else:
        return JsonResponse({'mensaje': 'Método no permitido'}, status=405)

def proceso_adopcion(request):
    data = json.loads(request.body)
    # Obtener datos de la solicitud (id_usuario, mascota, comentarios)
    id_usuario = data.get('id_usuario')
    id_mascota = data.get('mascota')
    comentarios = data.get('comentarios')
    fecha_visita = data.get('fecha_visita')
    persona = Persona.objects.get(user__id=id_usuario)

    # Verificar si ya hay una solicitud pendiente para esta mascota y usuario
    if Adopcion.objects.filter(usuario_adoptante_id=persona.id, mascota_id=id_mascota, estado_adopcion__estado='Pendiente').exists():
        return JsonResponse({'message': 'Ya tienes una solicitud pendiente para esta mascota','estado':False}, status=400)

    # Verificar si la mascota ya tiene una adopción aprobada
    if Adopcion.objects.filter(mascota_id=id_mascota, estado_adopcion__estado='Aprobado').exists():
        return JsonResponse({'message': 'Esta mascota ya ha sido adoptada por otra persona','estado':False}, status=400)

    # Crear la nueva solicitud de adopción
    estado_pendiente = EstadoAdopcion.objects.get(estado='Pendiente')
    Adopcion.objects.create(
        usuario_adoptante_id=persona.id,
        mascota_id=id_mascota,
        estado_adopcion=estado_pendiente,
        fecha_visita=fecha_visita,
        comentarios=comentarios
    )

    return JsonResponse({'message': 'Solicitud Enviada Correctamente','estado':True}, status=200)