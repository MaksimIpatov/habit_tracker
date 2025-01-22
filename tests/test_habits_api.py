from django.urls import reverse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.test import APITestCase
from rest_framework_simplejwt.tokens import RefreshToken

from habits.models import Habit
from users.models import User


class HabitTests(APITestCase):
    user: User
    another_user: User
    habit: Habit
    user_token: str
    another_user_token: str

    def setUp(self) -> None:
        self.user = User.objects.create_user(
            email="test_user@mail.ru",
            password="password123",
        )
        self.another_user = User.objects.create_user(
            email="another_user@mail.ru",
            password="password123",
        )
        self.habit = Habit.objects.create(
            user=self.user,
            action="Прогулка",
            place="Парк",
            time="08:00",
            execution_time=120,
            periodicity=1,
            is_pleasant=False,
            is_public=True,
        )
        self.user_token = str(
            RefreshToken.for_user(self.user).access_token,
        )
        self.another_user_token = str(
            RefreshToken.for_user(self.another_user).access_token
        )
        self.client.credentials(
            HTTP_AUTHORIZATION=f"Bearer {self.user_token}",
        )

    def test_create_habit(self) -> None:
        url: str = reverse("api:habit-list")
        data: dict[str, str | int | bool] = {
            "action": "Чтение",
            "place": "Дом",
            "time": "20:00",
            "execution_time": 60,
            "periodicity": 1,
            "is_pleasant": False,
            "is_public": False,
        }

        response: Response = self.client.post(
            url,
            data,
            format="json",
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED,
        )
        self.assertEqual(Habit.objects.count(), 2)

    def test_list_habits(self) -> None:
        url: str = reverse("api:habit-list")

        response: Response = self.client.get(url, format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data["results"]), 1)

    def test_list_public_habits(self) -> None:
        url: str = reverse("api:habit-list") + "?public=1"
        self.client.credentials(
            HTTP_AUTHORIZATION=f"Bearer {self.another_user_token}"
        )

        response: Response = self.client.get(url, format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data["results"]), 1)
        self.assertEqual(
            response.data["results"][0]["is_public"],
            True,
        )

    def test_update_habit_as_owner(self) -> None:
        url: str = reverse(
            "api:habit-detail",
            kwargs={"pk": self.habit.id},
        )
        data: dict[str, str | int] = {
            "action": "Бег",
            "place": "Стадион",
            "execution_time": 90,
        }

        response: Response = self.client.patch(
            url,
            data,
            format="json",
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.habit.refresh_from_db()
        self.assertEqual(self.habit.action, data["action"])

    def test_update_habit_as_not_owner(self) -> None:
        url: str = reverse(
            "api:habit-detail",
            kwargs={"pk": self.habit.id},
        )
        self.client.credentials(
            HTTP_AUTHORIZATION=f"Bearer {self.another_user_token}"
        )
        data: dict[str, str] = {"action": "Медитация"}

        response: Response = self.client.patch(
            url,
            data,
            format="json",
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_403_FORBIDDEN,
        )

    def test_delete_habit_as_owner(self) -> None:
        url: str = reverse(
            "api:habit-detail",
            kwargs={"pk": self.habit.id},
        )

        response: Response = self.client.delete(url, format="json")

        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT,
        )
        self.assertEqual(Habit.objects.count(), 0)

    def test_delete_habit_as_not_owner(self) -> None:
        url: str = reverse(
            "api:habit-detail",
            kwargs={"pk": self.habit.id},
        )
        self.client.credentials(
            HTTP_AUTHORIZATION=f"Bearer {self.another_user_token}"
        )

        response: Response = self.client.delete(url, format="json")

        self.assertEqual(
            response.status_code,
            status.HTTP_403_FORBIDDEN,
        )
