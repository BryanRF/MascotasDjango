from django.urls import path
from . import views

urlpatterns = [
    # URLs para Donacion
    path('donacion/create/', views.donacion_create, name='donacion_create'),
    path('donacion/list/', views.donacion_list, name='donacion_list'),

    # URLs para Evento
    path('evento/create/', views.evento_create, name='evento_create'),
    path('evento/list/', views.evento_list, name='evento_list'),

    # URLs para EventoParticipante
    path('evento_participante/create/', views.evento_participante_create, name='evento_participante_create'),
    path('evento_participante/list/', views.evento_participante_list, name='evento_participante_list'),

    # URLs para Premio
    path('premio/create/', views.premio_create, name='premio_create'),
    path('premio/list/', views.premio_list, name='premio_list'),

    # URLs para Ganador
    path('ganador/create/', views.ganador_create, name='ganador_create'),
    path('ganador/list/', views.ganador_list, name='ganador_list'),
]
