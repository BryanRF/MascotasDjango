from django.db import models
import uuid
from django.contrib.auth.models import User
from PIL import Image
from django.contrib.auth import authenticate, login

class Persona(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)
    nombre = models.CharField(max_length=100)
    telefono = models.CharField(max_length=15)
    dni = models.CharField(max_length=15)
    email = models.EmailField()
    fecha_nacimiento = models.DateField()
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    def save(self, *args, **kwargs):
        self.nombre = ' '.join(part.capitalize() for part in self.nombre.split())
        super().save(*args, **kwargs)
    def clean(self):
        self.email = self.email.lower().strip()
        super().clean()
    def login_persona(request, username, password):
        # Obtener el usuario asociado a la persona
        persona = Persona.objects.get(user__username=username)
        
        # Autenticar al usuario
        user = authenticate(username=username, password=password)
        
        if user is not None:
            login(request, user)
            return True
        else:
            return False    
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
    imagen = models.ImageField(upload_to='imagenes_mascotas/',null=True)
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if self.imagen:
            img = Image.open(self.imagen.path)
            img.thumbnail((300, 300))
            img.save(self.imagen.path, 'WEBP')
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
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if self.imagen:
            img = Image.open(self.imagen.path)
            img.thumbnail((300, 300))
            img.save(self.imagen.path, 'WEBP')
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
    mascota = models.ForeignKey(Mascota, on_delete=models.CASCADE)
    fecha_adopcion = models.DateField(null=True, blank=True)
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


class VisitaAdopcion(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)
    fecha_visita = models.DateField()
    mascota = models.ForeignKey(Mascota, on_delete=models.CASCADE)  
    adoptante = models.ForeignKey(Persona, on_delete=models.CASCADE)  
    asistio = models.BooleanField(default=False,null=True) 

    def __str__(self):
        return f"Visita el {self.fecha_visita} de adopción para {self.mascota.nombre} por {self.adoptante.nombre}."
    
    
class VisitaGeneral(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)
    fecha_visita = models.DateField()
    persona = models.ForeignKey(Persona, on_delete=models.CASCADE)
    asistio = models.BooleanField(default=False,null=True) 

    def __str__(self):
        return f"Visita el {self.fecha_visita} de {self.persona.nombre} | asistió: {self.persona.asistio}."


class Donacion(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)
    descripcion = models.TextField()
    fecha_donacion = models.DateField()
    persona = models.ForeignKey(Persona, on_delete=models.CASCADE)

    def __str__(self):
        return f"Donación de {self.persona.nombre} de {self.descripcion} el {self.fecha_donacion}."
    
    
class Evento(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)
    nombre = models.CharField(max_length=300)
    fecha_inicio = models.DateField()
    fecha_fin_participacion = models.DateField()
    costo_participacion = models.DecimalField(max_digits=10, decimal_places=2)
    recaudacion = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return f"Evento: {self.nombre} el {self.fecha_inicio}."

class EventoParticipante(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE)
    participante = models.ForeignKey(Persona, on_delete=models.CASCADE)
    ticket = models.PositiveIntegerField(unique=True)  # Campo para el número de ticket único
    def save(self, *args, **kwargs):
        self.evento.recaudacion += self.evento.costo_participacion
        self.evento.save()
        super().save(*args, **kwargs)
    def save(self, *args, **kwargs):
        # Verificar si es un nuevo registro o una actualización
        if not self.id:
            # Es un nuevo registro, asignar número de ticket
            ultimo_ticket = EventoParticipante.objects.filter(evento=self.evento).order_by('-ticket').first()
            if ultimo_ticket:
                self.ticket = ultimo_ticket.ticket + 1
            else:
                self.ticket = 1

        super().save(*args, **kwargs)

    def __str__(self):
        return f"Participante: {self.participante.nombre} en Evento: {self.evento.nombre}, Ticket: {self.ticket}"

class Premio(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.nombre

class Ganador(models.Model):
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE)
    premio = models.ForeignKey(Premio, on_delete=models.CASCADE)
    participante = models.ForeignKey(EventoParticipante, on_delete=models.CASCADE)

    def __str__(self):
        return f"Ganador: {self.participante.participante.nombre} en Evento: {self.evento.nombre}, Premio: {self.premio.nombre}"