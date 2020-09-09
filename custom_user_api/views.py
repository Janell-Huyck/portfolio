from rest_framework.viewsets import ModelViewSet
from custom_user_api.serializers import CustomUserSerializer
from custom_user.models import CustomUser


class CustomUserViewSet(ModelViewSet):
    """Returns all users"""

    serializer_class = CustomUserSerializer
    queryset = CustomUser.objects.all()

