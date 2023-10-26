from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
import json
from django.shortcuts import render, redirect
from .forms import PersonaForm, DireccionForm, UsuarioRegistroForm, UsuarioLoginForm
from api.models import Persona, Direccion
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth import logout


def persona_create(request):
    if request.method == 'POST':
        form = PersonaForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({'success': True, 'message': 'Persona creada exitosamente'})
        else:
            return JsonResponse({'success': False, 'errors': form.errors})
    else:
        form = PersonaForm()
    return render(request, 'persona/persona_form.html', {'form': form})


def persona_list(request):
    personas = Persona.objects.all()
    personas_serializadas = []
    for persona in personas:
        persona_serializada = {
            'id': str(persona.id),
            'nombre': persona.nombre,
            'telefono': persona.telefono,
            'dni': persona.dni,
            'email': persona.email,
            'fecha_nacimiento': persona.fecha_nacimiento.strftime('%Y-%m-%d'),
        }
        personas_serializadas.append(persona_serializada)
    return JsonResponse({'personas': personas_serializadas})


def direccion_create(request, persona_id):
    if request.method == 'POST':
        form = DireccionForm(request.POST)
        if form.is_valid():
            direccion = form.save(commit=False)
            direccion.persona = Persona.objects.get(id=persona_id)
            direccion.save()
            return JsonResponse({'success': True, 'message': 'Dirección creada exitosamente'})
        else:
            return JsonResponse({'success': False, 'errors': form.errors})
    else:
        form = DireccionForm()
    return render(request, 'direccion/direccion_form.html', {'form': form})


def direccion_list(request, persona_id):
    direcciones = Direccion.objects.filter(persona__id=persona_id)
    direcciones_serializadas = []
    for direccion in direcciones:
        direcciones_serializadas.append({
            'id': str(direccion.id),
            'direccion': direccion.direccion,
        })
    return JsonResponse({'direcciones': direcciones_serializadas})


def usuario_registro(request):
    if request.method == 'POST':
        form = UsuarioRegistroForm(request.POST)
        if form.is_valid():
            # Crear el usuario
            user = form.save()

            # Crear la persona
            persona = Persona.objects.create(
                user=user,
                nombre=form.cleaned_data.get('nombre'),
                telefono=form.cleaned_data.get('telefono'),
                dni=form.cleaned_data.get('dni'),
                email=form.cleaned_data.get('email'),
                fecha_nacimiento=form.cleaned_data.get('fecha_nacimiento')
            )

            # Crear la dirección (si aplica)
            direccion_form = DireccionForm(request.POST)
            if direccion_form.is_valid():
                Direccion.objects.create(
                    persona=persona,
                    direccion=direccion_form.cleaned_data.get('direccion')
                )

            # Autenticar al usuario
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)

            return redirect('persona_create')
    else:
        form = UsuarioRegistroForm()
    return render(request, 'usuario/registro.html', {'form': form})


def usuario_login(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        username = data.get('username')
        password = data.get('password')

        # Autenticar al usuario
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'success': False, 'error': 'Credenciales inválidas'})


def logout_view(request):
    logout(request)
    # Redirige a donde quieras después del cierre de sesión
    return redirect('inicio')


def get_datos(request, usuario_id):
    try:
        usuario = User.objects.get(id=usuario_id)
        persona = Persona.objects.get(user=usuario)
        datos = {
            'id': persona.id,
            'nombre': persona.nombre,
            'telefono': persona.telefono,
            'dni': persona.dni,
            'email': persona.email,
            'fecha_nacimiento': str(persona.fecha_nacimiento),
        }

        return JsonResponse({'success': True, 'datos': datos})
    except User.DoesNotExist:
        return JsonResponse({'success': False, 'error': 'El usuario no existe'})
    except Persona.DoesNotExist:
        return JsonResponse({'success': False, 'error': 'La persona no existe'})


def editar_persona(request, persona_id):
    if request.method == 'PUT':
        data = json.loads(request.body)
        nuevo_nombre = data.get('nombre')
        nuevo_telefono = data.get('telefono')
        nuevo_dni = data.get('dni')
        nuevo_email = data.get('email')
        nueva_fecha_nacimiento = data.get('fecha_nacimiento')
        try:
            persona = Persona.objects.get(id=persona_id)
            persona.nombre = nuevo_nombre
            persona.telefono = nuevo_telefono
            persona.dni = nuevo_dni
            persona.email = nuevo_email
            persona.fecha_nacimiento = nueva_fecha_nacimiento
            persona.save()

            return JsonResponse({'success': True, 'message': 'Cambios guardados exitosamente'})
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)}, status=500)
    else:
        return JsonResponse({'success': False, 'error': 'Método no permitido'}, status=405)
