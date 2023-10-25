from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

from rest_framework.viewsets import ViewSet


# controller decorado
class ProtectedController(ViewSet):
    api_view(['GET', 'POST'])
    authentication_classes([JWTAuthentication])
    permission_classes([IsAuthenticated])

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
