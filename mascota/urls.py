from django.urls import path
# from django.contrib.auth.decorators import login_required
from . import views
# from mascota.views import index, mascota_view, mascota_list, mascota_edit, mascota_delete, mascota_like

urlpatterns = [
    path('adopcion/', (views.index), name='adopcion'),
    path('proceso-adopcion/', views.proceso_adopcion, name='proceso_adopcion'),
    path('api_lista/', views.mascota_list, name='mascota_list'),
    path('lista/<int:id_usuario>/', views.mascota_usuario_list, name='mascota_usuario_list'),
    path('datatables_lista/<int:id_usuario>', views.mascota_datatables_list, name='mascota_datatables_list'),
    path('mascota_like/<uuid:id_mascota>/', views.mascota_like, name='mascota_like'),
    path('obtener/<uuid:id_mascota>', views.mascota_id_list, name='mascota_id_list'),
]
