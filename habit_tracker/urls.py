from django.contrib import admin
from django.urls import include, path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="Habit Tracker API Docs",
        default_version="v1",
        description="Habit Tracker API description",
        terms_of_service="https://www.habittracker.com/policies/terms/",
        contact=openapi.Contact(email="contact@habittracker.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("api.urls", namespace="api")),
    path("users/", include("users.urls", namespace="users")),
    path(
        "swagger/",
        schema_view.with_ui("swagger", cache_timeout=10),
        name="schema-swagger-ui",
    ),
    path(
        "redoc/",
        schema_view.with_ui("redoc", cache_timeout=10),
        name="schema-redoc",
    ),
]
