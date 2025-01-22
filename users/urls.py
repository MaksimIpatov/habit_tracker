from django.contrib.auth.views import LogoutView
from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from users.apps import UsersConfig
from users.views import (
    UserCreateAPIView,
    UserDestroyAPIView,
    UserListAPIView,
    UserRetrieveView,
    UserUpdateAPIView,
)

app_name = UsersConfig.name

urlpatterns = [
    path(
        "",
        UserListAPIView.as_view(),
        name="users-list",
    ),
    path(
        "register/",
        UserCreateAPIView.as_view(),
        name="register",
    ),
    path(
        "login/",
        TokenObtainPairView.as_view(),
        name="login",
    ),
    path(
        "logout/",
        LogoutView.as_view(),
        name="logout",
    ),
    path(
        "<int:pk>/edit/",
        UserUpdateAPIView.as_view(),
        name="users-edit",
    ),
    path(
        "<int:pk>/delete/",
        UserDestroyAPIView.as_view(),
        name="users-delete",
    ),
    path(
        "<int:pk>/",
        UserRetrieveView.as_view(),
        name="users-detail",
    ),
    path(
        "token/refresh/",
        TokenRefreshView.as_view(),
        name="token_refresh",
    ),
]
