from django.views import View
from django.http import JsonResponse
from .models import  Mascota,Persona,User
from django.core.exceptions import ObjectDoesNotExist
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
import json
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.urls import reverse
from .serializers import PersonaSerializer,MascotaSerializer
# from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
@method_decorator(csrf_exempt, name='dispatch')
class MascotaView(View):
    def put(self, request, mascota_id):
        try:
            mascota = Mascota.objects.get(id=mascota_id)
        except ObjectDoesNotExist:
            return JsonResponse({'error': 'Mascota no encontrada'}, status=404)

        mascota.like()
        return JsonResponse({'message': '¡Like agregado!', 'likes': mascota.likes})
    
@method_decorator(csrf_exempt, name='dispatch')
class PersonaView(View):
    def post(self, request):
        try:
            data = json.loads(request.body)
            username = data.get('username').strip()
            password = data.get('password').strip()
            nombre = data.get('nombre').strip()
            telefono = data.get('telefono').strip()
            dni = data.get('dni').strip()
            email = data.get('email').strip()
            fecha_nacimiento = data.get('fechaNacimiento').strip()
            # ajustar parametros 
            nombre = ' '.join(part.capitalize() for part in nombre.split())
            email = email.lower()
            username = username.lower()
            # Crear un nuevo usuario
            user = User.objects.create_user(username, email, password)
            
            # Crear una nueva persona asociada al usuario
            persona = Persona(
                user=user,
                nombre=nombre,
                telefono=telefono,
                dni=dni,
                email=email,
                fecha_nacimiento=fecha_nacimiento,
            )
            persona.save()

            print('Registro exitoso')
            print(user)

            return JsonResponse({'success': True})
        except Exception as e:
            print(f'Error: {str(e)}')
            return JsonResponse({'success': False, 'error': str(e)})

    def get(self, request, id):
        try:
            # Obtener la persona por su ID
            persona = Persona.objects.get(id=id)
            # Serializar los datos de la persona
            serializer = PersonaSerializer(persona)  # Asegúrate de tener un serializer para Persona definido
            # Devolver los datos serializados como respuesta JSON
            return JsonResponse(serializer.data)
        except Persona.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'La persona no existe'})
        
@method_decorator(csrf_exempt, name='dispatch')
class LoginView(View):
    def post(self, request):
        data = json.loads(request.body)
        username_or_email = data.get('username_or_email')
        password = data.get('password')

        # Verifica si el campo ingresado es un nombre de usuario o un correo electrónico
        user = None
        if '@' in username_or_email:
            user = authenticate(request, email=username_or_email, password=password)
        else:
            user = authenticate(request, username=username_or_email, password=password)

        if user is not None:
            login(request, user)
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'success': False, 'error': 'Credenciales incorrectas'})



    def get(self,request):
        logout(request)
        return redirect(reverse('inicio'))  # Puedes redirigir a donde desees después del cierre de sesión
    
    
@method_decorator(csrf_exempt, name='dispatch')
class MascotasDataTablesView(View):
     def get(self, request):
        mascotas = Mascota.objects.all()
        data = []
        draw = int(request.GET.get('draw', 1))  # Obtener el número de solicitud (draw)
        start = int(request.GET.get('start', 0))  # Índice de inicio de registros
        length = int(request.GET.get('length', 10)) 
        total_registros = Mascota.objects.count()

        # Filtrar registros si se proporciona algún criterio de búsqueda
        # Por ejemplo, si DataTables envía un parámetro de búsqueda como request.GET.get('search[value]')
        # puedes usar ese valor para realizar la búsqueda
        # mascotas = Mascota.objects.filter(nombre__icontains=request.GET.get('search[value]'))

        # Obtener registros paginados
        mascotas = Mascota.objects.all()[start:start + length]
        for mascota in mascotas:
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
        response = {
            'draw': draw,
            'recordsTotal': total_registros,
            'recordsFiltered': total_registros,  # En este caso, no hay filtrado, así que es igual a total_registros
            'data': data
        }    

        return JsonResponse(response, safe=False)

class MascotaAPIView(generics.ListAPIView):
    serializer_class = MascotaSerializer
    queryset = Mascota.objects.all()
    # filter_backends = [DjangoFilterBackend]
    filterset_fields = ['especie__nombre', 'codigo']