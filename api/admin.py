from django.contrib import admin
from .models import Persona, Mascota, Imagen, Comentario, Etiqueta, Direccion, Especie, Vacuna, EstadoAdopcion, Adopcion, EvaluacionAdopcion
class DireccionInline(admin.TabularInline):
    model = Direccion
class ImagenInline(admin.TabularInline):
    model = Imagen
    
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

class VacunaInline(admin.TabularInline):
    model = Vacuna



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
    list_display = ('usuario_adoptante', 'usuario_administrador', 'mascota', 'fecha_adopcion', 'estado_adopcion', 'comentarios')

@admin.register(EvaluacionAdopcion)
class EvaluacionAdopcionAdmin(admin.ModelAdmin):
    list_display = ('adopcion', 'calificacion', 'comentarios', 'fecha_evaluacion')

