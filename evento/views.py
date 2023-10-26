# views.py

from django.shortcuts import render, redirect
from .forms import DonacionForm, EventoForm, EventoParticipanteForm, PremioForm, GanadorForm
from api.models import Donacion, Evento, EventoParticipante, Premio, Ganador

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

# Vistas para Ganador
def ganador_create(request):
    if request.method == 'POST':
        form = GanadorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ganador_list')
    else:
        form = GanadorForm()
    return render(request, 'ganador/ganador_form.html', {'form': form})

def ganador_list(request):
    ganadores = Ganador.objects.all()
    return render(request, 'ganador/ganador_list.html', {'ganadores': ganadores})
