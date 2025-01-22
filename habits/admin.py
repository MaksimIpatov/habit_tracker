from django.contrib import admin

from habits.models import Habit


@admin.register(Habit)
class HabitAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "action",
        "time",
        "place",
        "is_pleasant",
        "is_public",
    )
    list_filter = ("is_pleasant", "is_public", "periodicity")
    search_fields = ("action", "user__email", "place")
    raw_id_fields = ("user", "linked_habit")
    ordering = ("user", "action")
