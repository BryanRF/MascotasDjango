from django.db import models
import uuid

class Persona(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)
    nombre = models.CharField(max_length=100)
    telefono = models.CharField(max_length=15)
    dni = models.CharField(max_length=15)
    email = models.EmailField()
    fecha_nacimiento = models.DateField()
    genero = models.CharField(max_length=10, choices=[('masculino', 'Masculino'), ('femenino', 'Femenino'), ('otro', 'Otro')])

    def __str__(self):
        return self.nombre

class Direccion(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)
    persona = models.ForeignKey(Persona, on_delete=models.CASCADE)
    direccion = models.TextField()

    def __str__(self):
        return self.direccion

class Especie(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Etiqueta(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Vacuna(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)
    nombre_vacuna = models.CharField(max_length=100)
    fecha_administracion = models.DateField()
    proxima_fecha_vacunacion = models.DateField()
    notas_adicionales = models.TextField()
    mascota = models.ForeignKey('Mascota', on_delete=models.CASCADE)

    def __str__(self):
        return f'Vacuna de {self.nombre_vacuna} para {self.mascota.nombre}'

class Mascota(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)
    codigo = models.CharField(max_length=10, unique=True, null=True)  # Campo para el código único
    nombre = models.CharField(max_length=100)
    especie = models.ForeignKey(Especie, on_delete=models.CASCADE)
    edad = models.IntegerField()
    descripcion = models.TextField()
    disponible = models.BooleanField(default=True)
    color = models.CharField(max_length=50)
    tamano = models.CharField(max_length=20)
    etiquetas = models.ManyToManyField(Etiqueta)
    genero = models.CharField(max_length=10, choices=[('macho', 'Macho'), ('hembra', 'Hembra')])
    likes = models.IntegerField(default=0)  # Agregar el campo "likes"

    def like(self):
        self.likes += 1
        self.save()
    def save(self, *args, **kwargs):
        if not self.codigo:
            self.codigo = str(uuid.uuid4().fields[-1])[:8].upper()  # Generar un código único
        super().save(*args, **kwargs)

    def __str__(self):
        return self.nombre

class Imagen(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)
    mascota = models.ForeignKey(Mascota, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='imagenes_mascotas/')

    def __str__(self):
        return f'Imagen de {self.mascota.nombre}'

class Comentario(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)
    mascota = models.ForeignKey(Mascota, on_delete=models.CASCADE)
    autor = models.ForeignKey(Persona, on_delete=models.CASCADE)
    contenido = models.TextField()
    fecha_publicacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comentario de {self.autor.nombre} en {self.mascota.nombre}'
    
class EstadoAdopcion(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)
    estado = models.CharField(max_length=100)

    def __str__(self):
        return self.estado
class Adopcion(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)
    usuario_adoptante = models.ForeignKey(Persona, on_delete=models.CASCADE, related_name='adopciones_realizadas')
    usuario_administrador = models.ForeignKey(Persona, on_delete=models.CASCADE, related_name='adopciones_gestionadas')
    mascota = models.ForeignKey(Mascota, on_delete=models.CASCADE)
    fecha_adopcion = models.DateField()
    estado_adopcion = models.ForeignKey(EstadoAdopcion, on_delete=models.CASCADE)
    comentarios = models.TextField()

    def __str__(self):
        return f'Adopción de {self.mascota.nombre} por {self.usuario_adoptante.nombre}'

class EvaluacionAdopcion(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)
    adopcion = models.ForeignKey(Adopcion, on_delete=models.CASCADE)
    calificacion = models.PositiveIntegerField()
    comentarios = models.TextField()
    fecha_evaluacion = models.DateField()

    def __str__(self):
        return f'Evaluación de adopción de {self.adopcion.mascota.nombre} por {self.adopcion.usuario_adoptante.nombre}'


