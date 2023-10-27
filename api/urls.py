from django.urls import path
from .views import  PersonaView
from django.conf import settings
from django.conf.urls.static import static
from .controller.eventos.evento_controller import EventoController
from .controller.personas.personas_controller import PersonasController


urlpatterns = [
    path('registro_usuario/', PersonaView.as_view(), name='registro_usuario'),
    path('registrar_ticket/', EventoController.regitrar_ticket, name='registrar_ticket'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
