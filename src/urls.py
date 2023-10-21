from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include,re_path
# from . import views
from .views import InicioView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),  # Reemplaza 'nombre_de_tu_aplicacion' con el nombre de tu aplicación
    # re_path(r'^(?P<path>.*)$', views.page_not_found),
    path('', InicioView.as_view(), name='inicio'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
