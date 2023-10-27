# views.py
import json
from django.shortcuts import render, redirect
from .forms import DonacionForm, EventoForm, EventoParticipanteForm, PremioForm, GanadorForm
from api.models import Donacion, Evento, EventoParticipante, Premio, Ganador,Persona
from django.http import JsonResponse

# Vistas para Donacion
def donacion_create(request):
    if request.method == 'POST':
        form = DonacionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('donacion_list')
    else:
        form = DonacionForm()
    return render(request, 'donacion/donacion_form.html', {'form': form})

def donacion_list(request):
    donaciones = Donacion.objects.all()
    return render(request, 'donacion/donacion_list.html', {'donaciones': donaciones})

# Vistas para Evento
def evento_create(request):
    if request.method == 'POST':
        form = EventoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('evento_list')
    else:
        form = EventoForm()
    return render(request, 'evento/evento_form.html', {'form': form})

def evento_list(request):
    eventos = Evento.objects.all()
    return render(request, 'evento/evento_list.html', {'eventos': eventos})

# Vistas para EventoParticipante
def evento_participante_create(request):
    if request.method == 'POST':
        form = EventoParticipanteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('evento_participante_list')
    else:
        form = EventoParticipanteForm()
    return render(request, 'evento_participante/evento_participante_form.html', {'form': form})

def evento_participante_list(request):
    participantes = EventoParticipante.objects.all()
    return render(request, 'evento_participante/evento_participante_list.html', {'participantes': participantes})

# Vistas para Premio
def premio_create(request):
    if request.method == 'POST':
        form = PremioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('premio_list')
    else:
        form = PremioForm()
    return render(request, 'premio/premio_form.html', {'form': form})

def premio_list(request):
    premios = Premio.objects.all()
    return render(request, 'premio/premio_list.html', {'premios': premios})

def ganador_list(request):
    ganadores = Ganador.objects.all()
    return render(request, 'ganador/ganador_list.html', {'ganadores': ganadores})


def eventos_usuario_list(request, id_usuario):
    persona = Persona.objects.get(user__id=id_usuario)
    participaciones = EventoParticipante.objects.filter(participante=persona)
    eventos_participados = [participacion.evento for participacion in participaciones]
    contexto = {'eventos_participados': eventos_participados}
    return render(request, 'lista_eventos_usuario.html', contexto)

def eventos_usuario_info(request, id_usuario):
    try:
        eventos_participante = EventoParticipante.objects.filter(participante__user__id=id_usuario)
        data = []

        for participacion in eventos_participante:
            data.append({
                'nombre_evento': participacion.evento.nombre,
                'fecha_inicio': participacion.evento.fecha_inicio.strftime("%Y-%m-%d"),
                'fecha_fin_participacion': participacion.evento.fecha_fin_participacion.strftime("%Y-%m-%d"),
                'costo_participacion': str(participacion.evento.costo_participacion),
                'ticket': participacion.ticket,
            })

        return JsonResponse(data, safe=False)
    except EventoParticipante.DoesNotExist:
        return JsonResponse({'error': 'Usuario no encontrado'}, status=404)
    
    
from django.utils import timezone

def registrar_ticket(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        usuario_id = data.get('usuarioId')
        cantidad = data.get('cantidad')
        evento_id = data.get('eventoId')
    
        try:
            # Verificamos si el usuario y el evento existen
            persona = Persona.objects.get(user__id=usuario_id)
            evento = Evento.objects.get(pk=evento_id)

            # Verificamos si el evento ha finalizado
            if evento.fecha_fin_participacion < timezone.now().date():
                return JsonResponse({'message': 'El evento ha finalizado', 'icon': 'error', 'title': 'Error'}, status=400)

            # Convertimos la cantidad a un entero
            cantidad = int(cantidad)

            # Verificamos si hay suficientes boletos disponibles
            for _ in range(cantidad):
                evento_participante = EventoParticipante(evento=evento, participante=persona)
                evento_participante.save()

            return JsonResponse({'message': 'Tickets registrados correctamente', 'icon': 'success', 'title': 'Éxito'}, status=200)
        
        except Persona.DoesNotExist:
            return JsonResponse({'message': 'El usuario no existe', 'icon': 'error', 'title': 'Error'}, status=400)
        except Evento.DoesNotExist:
            return JsonResponse({'message': 'El evento no existe', 'icon': 'error', 'title': 'Error'}, status=400)
        except Exception as e:
            return JsonResponse({'message': str(e), 'icon': 'error', 'title': 'Error'}, status=500)

    else:
        return JsonResponse({'message': 'Método no permitido', 'icon': 'error', 'title': 'Error'}, status=405)
