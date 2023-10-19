from django.db import models

class Persona(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.TextField()
    telefono = models.CharField(max_length=15)
    email = models.EmailField()

    def __str__(self):
        return self.nombre

class Mascota(models.Model):
    ESPECIES_CHOICES = [
        ('perro', 'Perro'),
        ('gato', 'Gato'),
        ('otro', 'Otro'),
    ]

    nombre = models.CharField(max_length=100)
    especie = models.CharField(max_length=10, choices=ESPECIES_CHOICES)
    raza = models.CharField(max_length=50)  # Nueva adición: campo para raza
    edad = models.IntegerField()
    descripcion = models.TextField()
    disponible = models.BooleanField(default=True)

    # Características
    color = models.CharField(max_length=50)
    tamano = models.CharField(max_length=20)

    # Dueño (opcional)
    persona = models.ForeignKey(Persona, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.nombre

class Imagen(models.Model):
    mascota = models.ForeignKey(Mascota, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='imagenes_mascotas/')

    def __str__(self):
        return f'Imagen de {self.mascota.nombre}'

class Comentario(models.Model):
    mascota = models.ForeignKey(Mascota, on_delete=models.CASCADE)
    autor = models.ForeignKey(Persona, on_delete=models.CASCADE)
    contenido = models.TextField()
    fecha_publicacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comentario de {self.autor.nombre} en {self.mascota.nombre}'

class Etiqueta(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre
