from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include,re_path
# from . import views
from .views import InicioView,MascotasView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),  
    # re_path(r'^(?P<path>.*)$', views.page_not_found),
    path('', InicioView.as_view(), name='inicio'),
    path('mascotas', MascotasView.as_view(), name='mascotas'),
    
    # path('nosotros', InicioView.as_view(), name='nosotros'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
