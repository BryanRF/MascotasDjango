import json
from api.models import Persona

def serialize_persona(persona):
    serialized_persona = {
        'id': str(persona.id),
        'nombre': persona.nombre,
        'telefono': persona.telefono,
        'dni': persona.dni,
        'email': persona.email,
        'fecha_nacimiento': persona.fecha_nacimiento.strftime('%Y-%m-%d'),
    }
    return json.dumps(serialized_persona)
