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

class PremioInline(admin.TabularInline):
    model = Premio

class GanadorInline(admin.TabularInline):
    model = Ganador

class EventoParticipanteInline(admin.TabularInline):
    model = EventoParticipante

@admin.register(Evento)
class EventoAdmin(admin.ModelAdmin):
    inlines = [PremioInline, GanadorInline, EventoParticipanteInline]
    max_premios = 5
    min_premios = 3

    def get_formsets_with_inlines(self, request, obj=None):
        for inline in self.get_inline_instances(request, obj):
            yield inline.get_formset(request, obj), inline

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        if obj.premio_set.count() < self.min_premios:
            return [PremioInline]
        elif obj.premio_set.count() >= self.max_premios:
            return []
        return [PremioInline]


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

