from ..controller import Controller
from ..response import Response
from ...models import Persona
import json
from django.contrib.auth import authenticate, login
# from rest_framework_simplejwt.tokens import RefreshToken

class PersonasController(Controller):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.persona = Persona

    def login_usuario(self, request):
        try:
            data = json.loads(request.body)
            username_or_email = data.get('username_or_email')
            password = data.get('password')

            # Verifica si el campo ingresado es un nombre de usuario o un correo electrónico
            user = None
            if '@' in username_or_email:
                user = authenticate(request, email=username_or_email, password=password)
            else:
                user = authenticate(request, username=username_or_email, password=password)

            if user is not None:
                login(request, user)
                # Verifica las credenciales del usuario
                refresh= None
                return Response(code=200, title='Success', message='Usuario autenticado')
                
            else:
                return Response(code=401, title='Error', message='Credenciales incorrectas')
        except self.persona.DoesNotExist:
            return Response(code=401, title='Error', message='Credenciales incorrectas')
        except Exception as e:
            return Response(code=400, title='Error', message=str(e))


    # def opciones_list(self, request):
    #     try:
    #         id_usuario = str(request.user)
    #         id_database = request.GET.get('idDatabase')
    #         id_empresa = request.GET.get('idEmpresa')
    #         estado = request.GET.get('estado')
    #         data = self.cursor.select(
    #             'exec WebGetListOpcionesCmb %s,%s,%s,%s', (estado, id_usuario, id_database, id_empresa))

    #         return Response(code=200, message='Succesfull', data=data)
    #     except Exception as e:
    #         return Response(code=400, title='Error', message=str(e))

   