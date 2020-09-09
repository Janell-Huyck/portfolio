from django.conf.urls import include, url
from rest_framework import routers

from custom_user_api.views import CustomUserViewSet

router = routers.DefaultRouter()

router.register(r"CustomUser", CustomUserViewSet)

urlpatterns = [url(r"^custom_user_api/", include(router.urls))]
