from django.urls import path
# from django.contrib.auth.decorators import login_required
from . import views
# from mascota.views import index, mascota_view, mascota_list, mascota_edit, mascota_delete, mascota_like

urlpatterns = [
    path('adopcion/', (views.index), name='adopcion'),
    path('proceso-adopcion/', views.proceso_adopcion, name='proceso_adopcion'),
    # path('mascota_view/', views.mascota_view, name='mascota_view'),
    # path('mascota_list/', views.mascota_list, name='mascota_list'),
    # path('mascota_edit/<uuid:id_mascota>/', views.mascota_edit, name='mascota_edit'),
    # path('mascota_delete/<uuid:id_mascota>/', views.mascota_delete, name='mascota_delete'),
    path('mascota_like/<uuid:id_mascota>/', views.mascota_like, name='mascota_like'),
]
