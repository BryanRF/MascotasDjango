from django.urls import path
from . import views

urlpatterns = [
    path('info/<str:id_usuario>', views.eventos_usuario_info, name='eventos_usuario_info'),
    path('usuario/<str:id_usuario>/', views.eventos_usuario_list, name='eventos_usuario_list'),
    path('registrar_ticket/', views.registrar_ticket, name='registrar_ticket'),
]
