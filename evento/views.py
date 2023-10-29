# views.py
import json
from django.shortcuts import render, redirect
from .forms import  EventoForm, EventoParticipanteForm, PremioForm, GanadorForm
from api.models import  Evento, EventoParticipante, Premio, Ganador,Persona
from django.http import JsonResponse
from django.utils import timezone

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

def eventos_general_list(request, id_usuario=None):
    eventos = Evento.objects.all()

    if id_usuario:
        try:
            persona = Persona.objects.get(user__id=id_usuario)
            eventos_participados = EventoParticipante.objects.filter(participante=persona).values_list('evento', flat=True)
        except Persona.DoesNotExist:
            eventos_participados = []
    else:
        eventos_participados = []

    contexto = {'eventos_participados': eventos_participados, 'eventos': eventos}
    return render(request, 'lista_eventos_general.html', contexto)



def eventos_logeado_list(request, id_usuario):
    persona = Persona.objects.get(user__id=id_usuario)
    participaciones = EventoParticipante.objects.filter(participante=persona)
    eventos_participados = [participacion.evento for participacion in participaciones]

    # Verificar si el usuario participó en cada evento y construir un diccionario
    eventos_info = []
    for evento in Evento.objects.all():
        participo = evento in eventos_participados
        tiene_premio = evento.tiene_premio
        lista_premios = ", ".join([premio.nombre for premio in Premio.objects.filter(evento=evento)])
        finalizo = evento.finalizo
        ganadores = Ganador.objects.filter(evento=evento)

        eventos_info.append({
            'evento': evento,
            'usuario_participo': participo,
            'tiene_premio': tiene_premio,
            'lista_premios': lista_premios,
            'finalizo': finalizo,
            'ganadores': ganadores
        })

    contexto = {'eventos_info': eventos_info}
    return render(request, 'lista_eventos_logeado.html', contexto)


def eventos_usuario_info(request, id_usuario):
    try:
        eventos_participante = EventoParticipante.objects.filter(participante__user__id=id_usuario)
        data = []

        for participacion in eventos_participante:
            data.append({
                'nombre_evento': participacion.evento.nombre,
                'codigo': participacion.evento.codigo,
                'fecha_inicio': participacion.evento.fecha_inicio_formateada(),
                'fecha_fin_participacion': participacion.evento.fecha_fin_participacion_formateada(),
                'costo_participacion': "s/."+str(participacion.evento.costo_participacion),
                'ticket': participacion.ticket,
            })

        return JsonResponse(data, safe=False)
    except EventoParticipante.DoesNotExist:
        return JsonResponse({'error': 'Usuario no encontrado'}, status=404)
    
def eventos_general_info(request):
    try:
        eventos = Evento.objects.all()

        data = []

        for evento in eventos:
            evento_data = {
                'nombre_evento': evento.nombre,
                'fecha_inicio': evento.fecha_inicio_formateada(),
                'fecha_fin_participacion': evento.fecha_fin_participacion_formateada(),
                'costo_participacion': "s/. "+str(evento.costo_participacion),
                'recaudacion': "s/. "+str(evento.recaudacion),
                'finalizo': evento.finalizo,
                'tiene_premio': evento.tiene_premio,
                'codigo': evento.codigo,
                'premios': 'Sin premios registrados' ,
                'ganadores': 'Sin ganadores',
            }

            if evento.tiene_premio:
                premios = Premio.objects.filter(evento=evento)
                if premios:
                    premio_nombres = [premio.nombre for premio in premios]
                    premio_data = ', '.join(premio_nombres)
                    evento_data['premios'] = premio_data
                else:
                    evento_data['premios'] = 'Sin premios registrados'  
                if evento.finalizo:
                    ganadores = Ganador.objects.filter(evento=evento)
                    ganadores_data = []
                    for ganador in ganadores:
                        ganadores_data.append(f"{ganador.participante.participante.nombre} - {ganador.premio.nombre}")
                    ganadores_str = ', '.join(ganadores_data)
                    evento_data['ganadores'] = ganadores_str
              

            data.append(evento_data)

        return JsonResponse(data, safe=False)
    except Evento.DoesNotExist:
        return JsonResponse({'error': 'Eventos no encontrados'}, status=404)


    


def registrar_ticket(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        usuario_id = data.get('usuarioId')
        cantidad = data.get('cantidad')
        evento_id = data.get('eventoId')
        tickets_registrados = []    
    
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
                tickets_registrados.append(evento_participante.ticket)
                
                # Actualizamos la recaudación del evento
                evento.recaudacion += evento.costo_participacion
                evento.save()

            return JsonResponse({'tickets_registrados': tickets_registrados,'message': 'Tickets registrados correctamente', 'icon': 'success', 'title': 'Éxito'}, status=200)
        
        except Persona.DoesNotExist:
            return JsonResponse({'message': 'El usuario no existe', 'icon': 'error', 'title': 'Error'}, status=400)
        except Evento.DoesNotExist:
            return JsonResponse({'message': 'El evento no existe', 'icon': 'error', 'title': 'Error'}, status=400)
        except Exception as e:
            return JsonResponse({'message': str(e), 'icon': 'error', 'title': 'Error'}, status=500)

    else:
        return JsonResponse({'message': 'Método no permitido', 'icon': 'error', 'title': 'Error'}, status=405)

