# adopcion/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('proceso-adopcion/', views.proceso_adopcion, name='proceso_adopcion'),
     path('solicitudes_adopcion/<int:id_usuario>', views.adopciones_info, name='solicitudes_adopcion'),
     path('adopciones_usuario_list/<int:id_usuario>', views.adopciones_usuario_list, name='adopciones_usuario_list'),
     path('eliminar/<uuid:id_adopcion>', views.adopciones_eliminar, name='adopciones_eliminar'),
]
