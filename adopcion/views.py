# views.py

from django.shortcuts import render, redirect
from .forms import AdopcionForm
from api.models import Adopcion
from django.contrib.auth.decorators import login_required

def adopcion_create(request):
    if request.method == 'POST':
        form = AdopcionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('adopcion_list')
    else:
        form = AdopcionForm()
    return render(request, 'adopcion/adopcion_form.html', {'form': form})
def adopcion_list(request):
    adopciones = Adopcion.objects.all()
    return render(request, 'adopcion/adopcion_list.html', {'adopciones': adopciones})
def adopcion_detail(request, id_adopcion):
    adopcion = Adopcion.objects.get(id=id_adopcion)
    return render(request, 'adopcion/adopcion_detail.html', {'adopcion': adopcion})
def adopcion_update(request, id_adopcion):
    adopcion = Adopcion.objects.get(id=id_adopcion)
    if request.method == 'POST':
        form = AdopcionForm(request.POST, instance=adopcion)
        if form.is_valid():
            form.save()
            return redirect('adopcion_list')
    else:
        form = AdopcionForm(instance=adopcion)
    return render(request, 'adopcion/adopcion_form.html', {'form': form})
def adopcion_delete(request, id_adopcion):
    adopcion = Adopcion.objects.get(id=id_adopcion)
    if request.method == 'POST':
        adopcion.delete()
        return redirect('adopcion_list')
    return render(request, 'adopcion/adopcion_confirm_delete.html', {'adopcion': adopcion})
