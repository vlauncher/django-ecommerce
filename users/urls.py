from django.urls import include, path
from rest_framework import routers

from .views import ProfileViewSet

router = routers.DefaultRouter()
router.register("profiles", ProfileViewSet, basename="profiles")

urlpatterns = [
    path("", include(router.urls)),
]
