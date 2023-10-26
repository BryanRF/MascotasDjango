import json
from django.shortcuts import render, redirect
from .forms import PersonaForm, DireccionForm,UsuarioRegistroForm,UsuarioLoginForm
from api.models import Persona, Direccion
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
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

from django.contrib.auth import authenticate, login
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
        
from django.contrib.auth import logout

def logout_view(request):
    logout(request)
    # Redirige a donde quieras después del cierre de sesión
    return redirect('inicio')