from rest_framework.serializers import HyperlinkedModelSerializer

from custom_user.models import CustomUser


class CustomUserSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = CustomUser
        fields = "__all__"
        lookup_field = "username"

