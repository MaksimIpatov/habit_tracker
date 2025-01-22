from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from api.permissions import IsOwner
from api.serializers import HabitSerializer
from habits.models import Habit


class HabitViewSet(ModelViewSet):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer

    def get_permissions(self):
        if self.action in ("destroy", "update", "partial_update"):
            permission_classes = [IsAuthenticated, IsOwner]
        else:
            permission_classes = [IsAuthenticated]

        return [permission() for permission in permission_classes]

    def get_queryset(self):
        if self.action == "list":
            if "public" in self.request.query_params:
                return Habit.objects.filter(is_public=True)
            return Habit.objects.filter(user=self.request.user)
        return super().get_queryset()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
