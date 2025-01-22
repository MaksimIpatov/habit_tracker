# Generated by Django 4.2.18 on 2025-01-22 06:30

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Habit",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "action",
                    models.CharField(max_length=255, verbose_name="Действие"),
                ),
                (
                    "place",
                    models.CharField(
                        max_length=255, verbose_name="Место выполнения"
                    ),
                ),
                (
                    "reward",
                    models.CharField(
                        blank=True,
                        max_length=255,
                        null=True,
                        verbose_name="Вознаграждение",
                    ),
                ),
                (
                    "periodicity",
                    models.PositiveIntegerField(
                        default=1,
                        validators=[
                            django.core.validators.MinValueValidator(1),
                            django.core.validators.MaxValueValidator(7),
                        ],
                        verbose_name="Периодичность в днях",
                    ),
                ),
                (
                    "execution_time",
                    models.PositiveIntegerField(
                        validators=[
                            django.core.validators.MinValueValidator(7),
                            django.core.validators.MaxValueValidator(120),
                        ],
                        verbose_name="Время выполнения (в секундах)",
                    ),
                ),
                ("time", models.TimeField(verbose_name="Время выполнения")),
                (
                    "is_pleasant",
                    models.BooleanField(
                        default=False, verbose_name="Приятная привычка"
                    ),
                ),
                (
                    "is_public",
                    models.BooleanField(
                        default=False, verbose_name="Публичная привычка"
                    ),
                ),
                (
                    "linked_habit",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="linked_to",
                        to="habits.habit",
                        verbose_name="Связанная привычка",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="habits",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Пользователь",
                    ),
                ),
            ],
            options={
                "verbose_name": "Привычка",
                "verbose_name_plural": "Привычки",
                "ordering": ("-time", "user"),
            },
        ),
    ]
