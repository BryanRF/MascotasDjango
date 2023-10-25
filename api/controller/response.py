from rest_framework.response import Response as RestResponse


class Response(RestResponse):

    def __init__(self, code=None, title='', message='', data=None, other_data=None, message_error='', response_full=None):
        if data is None:
            data = []
        if other_data is None:
            other_data = []

        # if title == '' or title is None:
        #     match code:
        #         case 200:
        #             return "Operación Realizada Correctamente"
        #         case 300:
        #             return "Operación No Realizada"
        #         case 400:
        #             return "Error en la operación"

        response_data = {
            'status': code == 200,
            'code': code,
            'data': data,
            'otherData': other_data,
            'title': title,
            'message': message,
            'messageError': message_error,
            # 'response_full' : response_full
        }

        super().__init__(response_data)

    def format_errors(details):
        details = eval(details)
        cant_errors = 0
        cant_warnings = 0
        if details != '' and details is not None:
            for col in details:
                format_errors = []
                errors = col['error']
                errors_array = errors.split('||')
                for col2 in errors_array:
                    detail_array = col2.split('@')
                    if len(detail_array) > 0:
                        if detail_array[1] != '':
                            format_errors.append({
                                'label': detail_array[0],
                                'type': detail_array[1],
                                'message': detail_array[2],
                            })
                            if detail_array[1] == 'E':
                                cant_errors = cant_errors + 1
                            elif detail_array[1] == 'W':
                                cant_errors = cant_warnings + 1
                col['error'] = format_errors
        
        return { 
            # 'code': 400 if cant_errors > 0 else (300 if cant_warnings > 0 else 200),
            'code': 200,
            'title': 'Datos inválidos' if cant_errors > 0 else ('Datos con observaciones' if cant_warnings > 0 else 'Datos correctos'),
            'message': 'Algunos datos no son válidos' if cant_errors > 0 else ('Algunos datos tienen observaciones' if cant_warnings > 0 else 'Datos correctos'),
            'data': details 
        }
