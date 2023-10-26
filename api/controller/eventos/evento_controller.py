from ..controller import Controller
from ..response import Response
from ...models import Evento,EventoParticipante,Persona
import json

class EventoController(Controller):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.persona = Evento

    def regitrar_ticket(self, request):
        try:
            # Obtener datos del request
            data = json.loads(request.body)

            # Obtener el ID del usuario
            user_id = data.get('user_id')

            # Obtener la cantidad
            cantidad = data.get('cantidad')

            # Buscar a la persona correspondiente
            persona = Persona.objects.get(user__id=user_id)

            # Obtener el evento
            evento_id = data.get('evento_id')
            evento = Evento.objects.get(id=evento_id)

            # Crear el participante y asignar el ticket automáticamente
            participante = EventoParticipante(evento=evento, participante=persona)
            participante.save()

            # Actualizar la recaudación del evento
            evento.recaudacion += (evento.costo_participacion * cantidad)
            evento.save()

            return Response(code=200, message='Registrado Exitosamente', data=None)
        except Exception as e:
            return Response(code=400, title='Error', message=str(e))

   