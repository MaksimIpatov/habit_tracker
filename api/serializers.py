from rest_framework import serializers
from rest_framework.exceptions import ValidationError

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

    def validate(self, data):
        self.validate_reward_and_linked_habit(data)
        self.validate_linked_habit_is_pleasant(data)
        self.validate_pleasant_habit_constraints(data)

        return data

    def validate_reward_and_linked_habit(self, data):
        if data.get("reward") and data.get("linked_habit"):
            raise ValidationError(
                "Нельзя указать одновременно "
                "вознаграждение и связанную привычку.",
            )

    def validate_linked_habit_is_pleasant(self, data):
        linked_habit = data.get("linked_habit")

        if linked_habit and not linked_habit.is_pleasant:
            raise ValidationError(
                "Связанная привычка должна быть приятной.",
            )

    def validate_pleasant_habit_constraints(self, data):
        if data.get("is_pleasant") and (
            data.get("linked_habit") or data.get("reward")
        ):
            raise ValidationError(
                "Приятной привычке нельзя присвоить "
                "связанную привычку или вознаграждение.",
            )
