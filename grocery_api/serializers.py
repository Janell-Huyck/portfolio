from rest_framework.serializers import HyperlinkedModelSerializer

from grocery_list_backend.models import GroceryItem
from custom_user.models import CustomUser


class GroceryItemSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = GroceryItem
        basename = "grocery_item"
        fields = ("quantity", "item_name", "is_purchased", "shopper")


class CustomUserSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = CustomUser
        fields = ("display_name",)

