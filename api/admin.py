from django.contrib import admin
from .models import (
    Persona, Mascota, Evento, Imagen, Comentario, Etiqueta, 
    Direccion, Especie, Vacuna, EstadoAdopcion, Adopcion, 
      
    Premio, Ganador, EventoParticipante
)

class DireccionInline(admin.TabularInline):
    model = Direccion

class ImagenInline(admin.TabularInline):
    model = Imagen

class VacunaInline(admin.TabularInline):
    model = Vacuna

class GanadorInline(admin.TabularInline):
    model = Ganador
    extra = 1  # Esto determina cuántos campos adicionales de Ganador se mostrarán

@admin.register(Evento)
class EventoAdmin(admin.ModelAdmin):
    # Define los campos que quieres mostrar en la lista de eventos
    list_display = ('nombre', 'fecha_inicio', 'fecha_fin_participacion', 'costo_participacion', 'recaudacion', 'finalizo', 'tiene_premio')

    # Añade un campo de búsqueda
    search_fields = ['nombre']

    inlines = [GanadorInline]

@admin.register(Premio)
class PremioAdmin(admin.ModelAdmin):
    pass

@admin.register(Ganador)
class GanadorAdmin(admin.ModelAdmin):
    pass


  


@admin.register(Persona)
class PersonaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'telefono', 'email')
    inlines = [DireccionInline]

@admin.register(Especie)
class EspecieAdmin(admin.ModelAdmin):
    list_display = ('nombre',)

@admin.register(Etiqueta)
class EtiquetaAdmin(admin.ModelAdmin):
    list_display = ('nombre',)

@admin.register(Mascota)
class MascotaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'especie',  'edad', 'descripcion', 'disponible', 'color', 'tamano','codigo','likes','genero')
    list_filter = ('especie', 'disponible')
    search_fields = ('nombre', 'codigo')
    inlines = [ImagenInline, VacunaInline]
    readonly_fields = ('codigo',)  # Agrega esta línea

@admin.register(Imagen)
class ImagenAdmin(admin.ModelAdmin):
    list_display = ('mascota', 'imagen')

@admin.register(Comentario)
class ComentarioAdmin(admin.ModelAdmin):
    list_display = ('mascota', 'autor', 'contenido', 'fecha_publicacion')

@admin.register(EstadoAdopcion)
class EstadoAdopcionAdmin(admin.ModelAdmin):
    list_display = ('estado',)

@admin.register(Adopcion)
class AdopcionAdmin(admin.ModelAdmin):
    list_display = ('usuario_adoptante',  'mascota', 'fecha_adopcion', 'estado_adopcion', 'comentarios')

