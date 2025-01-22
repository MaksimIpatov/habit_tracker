from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models

from users.constants import (
    CITY_NAME_LEN,
    NULL_BLANK_TRUE,
    PHONE_NUMBER_LEN,
    TG_CHAT_ID_MAX_LEN,
)
from users.managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField("Email", unique=True)
    phone_number = models.CharField(
        "Номер телефона",
        max_length=PHONE_NUMBER_LEN,
        **NULL_BLANK_TRUE,
    )
    city = models.CharField(
        "Город",
        max_length=CITY_NAME_LEN,
        **NULL_BLANK_TRUE,
    )
    avatar = models.ImageField(
        "Фото профиля",
        upload_to="avatars/",
        **NULL_BLANK_TRUE,
    )
    tg_chat_id = models.CharField(
        "Telegram ID",
        max_length=TG_CHAT_ID_MAX_LEN,
        **NULL_BLANK_TRUE,
    )
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["password"]

    objects = UserManager()

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
        ordering = ("email",)

    def __str__(self) -> str:
        return str(self.email)
