from django.core.exceptions import ValidationError
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from habits.constants import (
    ACTION_MAX_LENGTH,
    MAX_EXECUTION_TIME_SECOND,
    MAX_PERIODIC_HABIT_IN_DAYS,
    MIN_EXECUTION_TIME_SECOND,
    MIN_PERIODIC_HABIT_IN_DAYS,
    NULL_BLANK_TRUE,
    PLACE_MAX_LENGTH,
    REWARD_MAX_LENGTH,
)
from users.models import User


class Habit(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="habits",
        verbose_name="Пользователь",
    )
    action = models.CharField(
        "Действие",
        max_length=ACTION_MAX_LENGTH,
    )
    place = models.CharField(
        "Место выполнения",
        max_length=PLACE_MAX_LENGTH,
    )
    linked_habit = models.ForeignKey(
        "self",
        on_delete=models.SET_NULL,
        related_name="linked_to",
        **NULL_BLANK_TRUE,
        verbose_name="Связанная привычка",
    )
    reward = models.CharField(
        "Вознаграждение",
        max_length=REWARD_MAX_LENGTH,
        **NULL_BLANK_TRUE,
    )
    periodicity = models.PositiveIntegerField(
        "Периодичность в днях",
        default=MIN_PERIODIC_HABIT_IN_DAYS,
        validators=[
            MinValueValidator(MIN_PERIODIC_HABIT_IN_DAYS),
            MaxValueValidator(MAX_PERIODIC_HABIT_IN_DAYS),
        ],
    )
    execution_time = models.PositiveIntegerField(
        "Время выполнения (в секундах)",
        validators=[
            MinValueValidator(MIN_EXECUTION_TIME_SECOND),
            MaxValueValidator(MAX_EXECUTION_TIME_SECOND),
        ],
    )
    time = models.TimeField(
        "Время выполнения",
    )
    is_pleasant = models.BooleanField(
        "Приятная привычка",
        default=False,
    )
    is_public = models.BooleanField(
        "Публичная привычка",
        default=False,
    )

    class Meta:
        verbose_name = "Привычка"
        verbose_name_plural = "Привычки"
        ordering = ("-time", "user")

    def validate_reward_or_linked_habit(self) -> None:
        if self.reward and self.linked_habit:
            raise ValidationError(
                "Нельзя указать одновременно "
                "вознаграждение и связанную привычку."
            )

    def validate_linked_habit_is_pleasant(self) -> None:
        if self.linked_habit and not self.linked_habit.is_pleasant:
            raise ValidationError(
                "Связанная привычка должна быть приятной.",
            )

    def clean_periodicity(self) -> None:
        if int(str(self.periodicity)) not in range(
            MIN_PERIODIC_HABIT_IN_DAYS,
            MAX_PERIODIC_HABIT_IN_DAYS,
        ):
            raise ValidationError(
                f"Периодичность должна быть от {MIN_PERIODIC_HABIT_IN_DAYS} "
                f"до {MAX_PERIODIC_HABIT_IN_DAYS} дней.",
            )

    def clean(self) -> None:
        self.validate_reward_or_linked_habit()
        self.validate_linked_habit_is_pleasant()

    def __str__(self) -> str:
        return str(self.action)
