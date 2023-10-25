from rest_framework import serializers
from .models import Persona, Mascota, Imagen, Comentario, Etiqueta, Especie

class PersonaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Persona
        fields = ['id', 'nombre', 'telefono', 'dni', 'email', 'fecha_nacimiento', 'genero', 'user']


class ComentarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comentario
        fields = ['id', 'mascota', 'autor', 'contenido', 'fecha_publicacion']
class EspecieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Especie
        fields = '__all__'

class EtiquetaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Etiqueta
        fields = '__all__'
class ImagenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Imagen
        fields = ['id', 'imagen']
class MascotaSerializer(serializers.ModelSerializer):
    especie = EspecieSerializer()
    etiquetas = EtiquetaSerializer(many=True)
    imagenes = ImagenSerializer(many=True)
    class Meta:
        model = Mascota
        fields = ['id', 'codigo', 'nombre', 'especie', 'edad', 'descripcion', 'disponible', 'color', 'tamano', 'etiquetas', 'genero', 'likes', 'imagenes']
