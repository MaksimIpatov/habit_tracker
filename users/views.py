from rest_framework.generics import (
    CreateAPIView,
    DestroyAPIView,
    ListAPIView,
    RetrieveAPIView,
    UpdateAPIView,
)
from rest_framework.permissions import IsAuthenticated

from api.serializers import UserSerializer
from users.models import User
from users.permissions import IsOwner
from users.serializers import UserProfileSerializer


class UserCreateAPIView(CreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def perform_create(self, serializer):
        user = serializer.save(is_active=True)
        user.set_password(user.password)
        user.save()


class UserUpdateAPIView(UpdateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = (IsOwner,)


class UserListAPIView(ListAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = (IsAuthenticated,)


class UserRetrieveView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = (IsAuthenticated,)


class UserDestroyAPIView(DestroyAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = (IsOwner,)
