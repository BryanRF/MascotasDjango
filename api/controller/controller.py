from rest_framework.decorators import api_view
from rest_framework.permissions import AllowAny
# from rest_framework_simplejwt.authentication import JWTAuthentication

from rest_framework.viewsets import ViewSet


# basic controller
class Controller(ViewSet):
    api_view(['GET', 'POST'])
    # authentication_classes = [JWTAuthentication]
    permission_classes = [AllowAny]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
