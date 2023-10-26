from django.urls import path
# from django.conf.urls import url, include
# from django.contrib.auth.decorators import login_required
from . import views
# from mascota.views import index, mascota_view, mascota_list, mascota_edit, mascota_delete, mascota_like

urlpatterns = [
    # ... otras rutas ...
    path('create/', views.persona_create, name='persona_create'),
    path('list/', views.persona_list, name='persona_list'),
    path('direccion/create/<str:persona_id>/', views.direccion_create, name='direccion_create'),
    path('direccion/list/<str:persona_id>/', views.direccion_list, name='direccion_list'),
    path('registro/', views.usuario_registro, name='usuario_registro'),
    path('login/', views.usuario_login, name='usuario_login'),
    path('logout/', views.logout_view, name='logout_view'),
    # ... otras rutas ...
]
