from django.conf.urls import include, url
from rest_framework import routers

from grocery_api.views import GroceryItemViewSet, CustomUserViewSet

router = routers.DefaultRouter()

router.register(r"grocery_list", GroceryItemViewSet, basename="grocery_item")
router.register(r"CustomUser", CustomUserViewSet)

urlpatterns = [url(r"^grocery_api/", include(router.urls))]
"""
from api.views import (GhostPostViewSet,
                       BoastViewSet,
                       RoastViewSet,)


router = routers.DefaultRouter()

router.register(r'roasts', RoastViewSet, basename='roasts')
router.register(r'boasts', BoastViewSet, basename='boasts')
router.register(r'ghostpost', GhostPostViewSet, basename='posts')


urlpatterns = [
    url(r'^api/', include(router.urls)),
]

"""
