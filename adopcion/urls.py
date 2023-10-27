# adopcion/urls.py

from django.urls import path
from . import views

urlpatterns = [

     path('solicitudes_adopcion/<int:id_usuario>', views.adopciones_info, name='solicitudes_adopcion'),
     path('adopciones_usuario_list/<int:id_usuario>', views.adopciones_usuario_list, name='adopciones_usuario_list'),
]
