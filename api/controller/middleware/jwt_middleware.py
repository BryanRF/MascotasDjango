from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.response import Response
from rest_framework.status import HTTP_401_UNAUTHORIZED
from django.http import JsonResponse

class JWTMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        auth = JWTAuthentication()

        try:
            user = auth.authenticate(request)
            # return user
            if user is not None:
                request.user = 'user'  # user[0] contains the user object
            else:
                return JsonResponse({'code': 401, 'status': False, 'message': 'Token is invalid'})
        except AuthenticationFailed as e:
            return JsonResponse({'code': 401, 'status': False, 'message': str(e)})
        except Exception as e:
            return JsonResponse({'code': 401, 'status': False, 'message': e})

        return self.get_response(request)

    # def _get_error_message(self, exception):
    #     if isinstance(exception, TokenExpiredException):
    #         return "token_expired"
    #     elif isinstance(exception, TokenBlacklistedException):
    #         return "token_blacklist"
    #     elif isinstance(exception, TokenInvalidException):
    #         return "token_invalid"
    #     else:
    #         return "token_required"