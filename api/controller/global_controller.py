from ..utils.cursor import Cursor
from ..utils.response import Response
from django.http import Http404

from .controller import Controller


class GlobalController(Controller):

    # constructor
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.cursor = Cursor()

    def get_list_empresas(self, request):
        try:
            id_database = request.GET.get('idDatabase')
            activo = request.GET.get('activo') if request.GET.get('activo') != '' else None
            id_usuario = str(request.user)

            data = self.cursor.select('exec GenGetListEmpresas %s, %s, %s', (
                id_database, activo, id_usuario,
            ))

            return Response(code=200, message='Listado de Empresas', data=data)
        except Exception as e:
            return Response(code=400, title='Error', message=str(e))
    
    def parametro_list(self, request):
        try:
            id_database = request.GET.get('idDatabase')
            id_empresa = request.GET.get('idEmpresa')
            usuario = request.GET.get('usuario')
            modulo = request.GET.get('modulo')
            grupo = request.GET.get('grupo')
            tabla = request.GET.get('tabla')

            data = self.cursor.select('exec GenGetListParametro %s, %s, %s, %s, %s, %s', (
                id_database, id_empresa, usuario, modulo, grupo, tabla,
            ))

            if data:
                return Response(code=200, message='Listado de Parametros', data=data)
            else:
                return Response(code=200, message='No se encontraron registros', data=data)
        except Exception as e:
            return Response(code=400, title='Error', message=str(e))

    def tiempo_campania_list(self, request):
        try:
            id_database = 'AGROVISIONCORP'
            id_empresa = request.GET.get('idEmpresa')
            version = request.GET.get('version')
            id_usuario = str(request.user)

            data = self.cursor.select('exec WebGetListTiempoCampania %s,%s,%s,%s', (
                id_database, id_empresa, version, id_usuario,
            ))

            return Response(code=200, message='Listado de años campaña', data=data)
        except Exception as e:
            return Response(code=400, title='Error', message=str(e))

    def cultivo_list(self, request):
        try:
            id_database = 'AGROVISIONCORP'
            id_empresa = request.GET.get('idEmpresa')
            estado = request.GET.get('estado')
            id_usuario = str(request.user)

            data = self.cursor.select('exec WebGetListCultivo %s,%s,%s,%s', (
                id_database, id_empresa, estado, id_usuario,
            ))

            return Response(code=200, message='Listado de cultivo', data=data)
        except Exception as e:
            return Response(code=400, title='Error', message=str(e))
