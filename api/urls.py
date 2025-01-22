from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.apps import ApiConfig
from api.viewsets import HabitViewSet

app_name = ApiConfig.name

router = DefaultRouter()
router.register(r"habits", HabitViewSet, basename="habit")

urlpatterns = [
    path("", include(router.urls)),
]
