from django.urls import path
from .views import PersonaView, MascotaView

urlpatterns = [
    path('personas/', PersonaView.as_view(), name='persona_list'),
    path('mascotas/', MascotaView.as_view(), name='mascota_list'),
]
