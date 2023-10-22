from django.urls import path
from .views import  MascotaView,PersonaView,LoginView
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    # path('personas', PersonaView.as_view(), name='persona_list'),
    # path('mascotas', MascotaView.as_view(), name='mascota_list'),
    path('like_mascota/<str:mascota_id>/', MascotaView.as_view(), name='like_mascota'),
    path('registro_usuario/', PersonaView.as_view(), name='registro_usuario'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LoginView.as_view(), name='logout_view'),


]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
