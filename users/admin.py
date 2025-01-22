from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from users.models import User


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    model = User
    list_display = ("email", "phone_number", "city", "is_active")
    search_fields = ("email", "phone_number", "city")
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        (
            "Личные данные",
            {
                "fields": (
                    "first_name",
                    "last_name",
                    "phone_number",
                    "city",
                    "avatar",
                )
            },
        ),
        (
            "Разрешения",
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                )
            },
        ),
        ("Дата и время", {"fields": ("last_login", "date_joined")}),
    )
    ordering = ("email",)
