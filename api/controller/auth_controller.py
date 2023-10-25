from django.http import JsonResponse
from django.contrib.auth.hashers import check_password
from django.db import connection

# from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView
from encriptation import Encriptation
from response import Response

from ..models import Persona

from .controller import Controller

from django.core.mail import send_mail, BadHeaderError
from django.conf import settings


class AuthController(TokenObtainPairView, Controller):

    # constructor
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def get_login(self, request, *args, **kwargs):
        try:

            id_usuario = request.data.get('idUsuario')
            password_aux = request.data.get('password')

            encriptador = Encriptation()
            password = encriptador.encript(password_aux)
            print(password)
            data = self.cursor.select(
                'exec WebCheckCredenciales %s,%s', (id_usuario, password))
            if (data[0]['code'] == 200):
                usuario = Persona(idusuario=id_usuario)
                refresh = RefreshToken.for_user(usuario)
                access_token = str(refresh.access_token)
                data = {'token': access_token}
            # access_token = RefreshToken.for_user(str(idusuario))
            # data = {'token': access_token}
            # return Response(code=200, title='Operacion realizada', message='Inicio de sesion valido', data=refresh)
            # return { 'usuario': usuario }
                return Response(code=200, title='Operacion realizada', message='Inicio de sesion valido', data=data)
            else:
                return Response(code=data[0]['code'], title=data[0]['title'], message=data[0]['message'], message_error=data[0]['message_error'])
        except Exception as e:
            return Response(code=400, title='Error', message=str(e))


