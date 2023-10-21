from rest_framework import serializers
from .models import Persona, Mascota, Imagen, Comentario, Etiqueta

class PersonaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Persona
        fields = ['id', 'nombre', 'direccion', 'telefono', 'email']

class MascotaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mascota
        fields = ['id', 'nombre', 'especie', 'raza', 'edad', 'descripcion', 'disponible', 'color', 'tamano', 'persona']

class ImagenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Imagen
        fields = ['id', 'mascota', 'imagen']

class ComentarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comentario
        fields = ['id', 'mascota', 'autor', 'contenido', 'fecha_publicacion']

class EtiquetaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Etiqueta
        fields = ['id', 'nombre']
