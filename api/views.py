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
            username = data.get('username')
            print(username)
            print(username)
            print(username)
            print(username)
            print(username)
            print(username)
            print(username)
            password = data.get('password')
            nombre = data.get('nombre')
            telefono = data.get('telefono')
            dni = data.get('dni')
            email = data.get('email')
            fecha_nacimiento = data.get('fechaNacimiento')
            genero = data.get('genero')

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
                genero=genero
            )
            persona.save()

            print('Registro exitoso')
            print(user)

            return JsonResponse({'success': True})
        except Exception as e:
            print(f'Error: {str(e)}')
            return JsonResponse({'success': False, 'error': str(e)})

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