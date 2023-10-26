from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include,re_path
# from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

# from . import views
from .views import InicioView,EventoView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),  
    path('persona/', include('persona.urls')),  
    path('mascota/', include('mascota.urls')),  
    path('', InicioView.as_view(), name='inicio'),
    path('ver_evento/<uuid:evento_id>/', EventoView.ver_evento, name='ver_evento'),
    # path('mascotas', MascotasView.as_view(), name='mascotas'),
    # path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
