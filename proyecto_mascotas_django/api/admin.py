from django.contrib import admin
from .models import Persona, Mascota, Imagen, Comentario, Etiqueta

@admin.register(Persona)
class PersonaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'direccion', 'telefono', 'email')

class ImagenInline(admin.TabularInline):
    model = Imagen

@admin.register(Mascota)
class MascotaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'especie', 'raza', 'edad', 'descripcion', 'disponible', 'color', 'tamano', 'persona')
    list_filter = ('especie', 'disponible')
    search_fields = ('nombre', 'raza')
    inlines = [ImagenInline]

@admin.register(Comentario)
class ComentarioAdmin(admin.ModelAdmin):
    list_display = ('mascota', 'autor', 'contenido', 'fecha_publicacion')

@admin.register(Etiqueta)
class EtiquetaAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
