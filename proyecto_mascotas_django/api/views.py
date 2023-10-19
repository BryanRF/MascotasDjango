from django.views import View
from django.http import JsonResponse
from .models import Persona, Mascota, Imagen, Comentario, Etiqueta
from django.core.exceptions import ObjectDoesNotExist
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator


# Decorador para desactivar CSRF (Solo para propósitos de ejemplo, NO lo hagas en un proyecto real sin medidas de seguridad adicionales)
@method_decorator(csrf_exempt, name='dispatch')
class PersonaView(View):
    def get(self, request):
        personas = Persona.objects.all()
        data = [{'id': persona.id, 'nombre': persona.nombre, 'direccion': persona.direccion, 
                 'telefono': persona.telefono, 'email': persona.email} for persona in personas]
        return JsonResponse(data, safe=False)

    def post(self, request):
        nombre = request.POST.get('nombre')
        direccion = request.POST.get('direccion')
        telefono = request.POST.get('telefono')
        email = request.POST.get('email')
        persona = Persona(nombre=nombre, direccion=direccion, telefono=telefono, email=email)
        persona.save()
        return JsonResponse({'message': 'Persona creada exitosamente!'})

    def put(self, request):
        persona_id = request.POST.get('id')
        try:
            persona = Persona.objects.get(id=persona_id)
        except ObjectDoesNotExist:
            return JsonResponse({'error': 'Persona no encontrada'}, status=404)

        nombre = request.POST.get('nombre')
        direccion = request.POST.get('direccion')
        telefono = request.POST.get('telefono')
        email = request.POST.get('email')

        persona.nombre = nombre
        persona.direccion = direccion
        persona.telefono = telefono
        persona.email = email
        persona.save()

        return JsonResponse({'message': 'Persona actualizada exitosamente!'})

    def delete(self, request):
        persona_id = request.POST.get('id')
        try:
            persona = Persona.objects.get(id=persona_id)
        except ObjectDoesNotExist:
            return JsonResponse({'error': 'Persona no encontrada'}, status=404)

        persona.delete()
        return JsonResponse({'message': 'Persona eliminada exitosamente!'})


@method_decorator(csrf_exempt, name='dispatch')
class MascotaView(View):
    def get(self, request):
        mascotas = Mascota.objects.all()
        data = [{'id': mascota.id, 'nombre': mascota.nombre, 'especie': mascota.especie, 
                 'raza': mascota.raza, 'edad': mascota.edad, 'descripcion': mascota.descripcion,
                 'disponible': mascota.disponible, 'color': mascota.color, 'tamano': mascota.tamano,
                 'persona': mascota.persona.nombre if mascota.persona else None} for mascota in mascotas]
        return JsonResponse(data, safe=False)

    def post(self, request):
        nombre = request.POST.get('nombre')
        especie = request.POST.get('especie')
        raza = request.POST.get('raza')
        edad = request.POST.get('edad')
        descripcion = request.POST.get('descripcion')
        disponible = request.POST.get('disponible')
        color = request.POST.get('color')
        tamano = request.POST.get('tamano')
        persona_id = request.POST.get('persona_id')

        persona = None
        if persona_id:
            try:
                persona = Persona.objects.get(id=persona_id)
            except ObjectDoesNotExist:
                return JsonResponse({'error': 'Persona no encontrada'}, status=404)

        mascota = Mascota(nombre=nombre, especie=especie, raza=raza, edad=edad, descripcion=descripcion, 
                          disponible=disponible, color=color, tamano=tamano, persona=persona)
        mascota.save()
        return JsonResponse({'message': 'Mascota creada exitosamente!'})

    def put(self, request):
        mascota_id = request.POST.get('id')
        try:
            mascota = Mascota.objects.get(id=mascota_id)
        except ObjectDoesNotExist:
            return JsonResponse({'error': 'Mascota no encontrada'}, status=404)

        nombre = request.POST.get('nombre')
        especie = request.POST.get('especie')
        raza = request.POST.get('raza')
        edad = request.POST.get('edad')
        descripcion = request.POST.get('descripcion')
        disponible = request.POST.get('disponible')
        color = request.POST.get('color')
        tamano = request.POST.get('tamano')
        persona_id = request.POST.get('persona_id')

        persona = None
        if persona_id:
            try:
                persona = Persona.objects.get(id=persona_id)
            except ObjectDoesNotExist:
                return JsonResponse({'error': 'Persona no encontrada'}, status=404)

        mascota.nombre = nombre
        mascota.especie = especie
        mascota.raza = raza
        mascota.edad = edad
        mascota.descripcion = descripcion
        mascota.disponible = disponible
        mascota.color = color
        mascota.tamano = tamano
        mascota.persona = persona
        mascota.save()

        return JsonResponse({'message': 'Mascota actualizada exitosamente!'})

    def delete(self, request):
        mascota_id = request.POST.get('id')
        try:
            mascota = Mascota.objects.get(id=mascota_id)
        except ObjectDoesNotExist:
            return JsonResponse({'error': 'Mascota no encontrada'}, status=404)

        mascota.delete()
        return JsonResponse({'message': 'Mascota eliminada exitosamente!'})
