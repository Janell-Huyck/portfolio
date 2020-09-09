from django.conf.urls import include, url
from rest_framework import routers

from grocery_api.views import GroceryItemViewSet, CustomUserViewSet

router = routers.DefaultRouter()

router.register(r"grocery_list", GroceryItemViewSet, basename="grocery_item")
router.register(r"CustomUser", CustomUserViewSet)

urlpatterns = [url(r"^grocery_api/", include(router.urls))]
