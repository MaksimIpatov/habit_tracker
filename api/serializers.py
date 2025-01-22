from rest_framework import serializers

from habits.models import Habit
from users.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "id",
            "email",
            "password",
            "phone_number",
            "city",
            "avatar",
            "is_staff",
            "is_active",
            "tg_chat_id",
        )
        read_only_fields = ("id",)


class HabitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habit
        fields = (
            "id",
            "user",
            "action",
            "time",
            "place",
            "is_pleasant",
            "linked_habit",
            "reward",
            "periodicity",
            "execution_time",
            "is_public",
        )
        read_only_fields = ("id", "user")
