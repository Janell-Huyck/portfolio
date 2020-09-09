from rest_framework.viewsets import ModelViewSet
from grocery_api.serializers import GroceryItemSerializer, CustomUserSerializer
from grocery_list_backend.models import GroceryItem
from custom_user.models import CustomUser


class GroceryItemViewSet(ModelViewSet):
    """Returns all grocery items for the requesting user"""

    basename = "grocery_item"
    serializer_class = GroceryItemSerializer

    def get_queryset(self):
        shopper = self.request.user
        if shopper.id:
            queryset = GroceryItem.objects.filter(shopper=shopper)
        else:
            queryset = []
        return queryset


class CustomUserViewSet(ModelViewSet):
    """Returns all users"""

    serializer_class = CustomUserSerializer
    queryset = CustomUser.objects.all()

