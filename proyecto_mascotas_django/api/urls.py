from django.urls import path
from .views import PersonaView, MascotaView
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('personas/', PersonaView.as_view(), name='persona_list'),
    path('mascotas/', MascotaView.as_view(), name='mascota_list'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
