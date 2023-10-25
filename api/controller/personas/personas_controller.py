from ..controller import Controller
from ..response import Response
from ...models import Persona
import json
from rest_framework_simplejwt.tokens import RefreshToken

class PersonasController(Controller):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.persona = Persona

    def login_usuario(self, request):
        try:
            usuario = request.data.get('username')
            password = request.data.get('password')

            # Verifica las credenciales del usuario
            user = self.persona.objects.get(username=usuario)

            if user.check_password(password):
                refresh = RefreshToken.for_user(user)

                return Response(
                    code=200,
                    message='Usuario autenticado',
                    data={
                        'user_id': user.id,
                        'access_token': str(refresh.access_token),
                        'refresh_token': str(refresh)
                    }
                )
            else:
                return Response(code=401, title='Error', message='Credenciales incorrectas')
        except self.persona.DoesNotExist:
            return Response(code=401, title='Error', message='Credenciales incorrectas')
        except Exception as e:
            return Response(code=400, title='Error', message=str(e))


    def opciones_list(self, request):
        try:
            id_usuario = str(request.user)
            id_database = request.GET.get('idDatabase')
            id_empresa = request.GET.get('idEmpresa')
            estado = request.GET.get('estado')
            data = self.cursor.select(
                'exec WebGetListOpcionesCmb %s,%s,%s,%s', (estado, id_usuario, id_database, id_empresa))

            return Response(code=200, message='Succesfull', data=data)
        except Exception as e:
            return Response(code=400, title='Error', message=str(e))

   