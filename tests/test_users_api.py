from rest_framework import status
from rest_framework.response import Response
from rest_framework.test import APITestCase

from users.models import User


class UserTests(APITestCase):
    def test_register_user(self) -> None:
        url: str = "/users/register/"
        data: dict[str, str] = {
            "email": "new_user@mail.ru",
            "password": "password123",
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
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(User.objects.first().email, data["email"])

    def test_login_user(self) -> None:
        user: User = User.objects.create_user(
            email="test_user@mail.ru",
            password="password123",
        )
        url: str = "/users/login/"
        data: dict[str, str] = {
            "email": user.email,
            "password": "password123",
        }

        response: Response = self.client.post(
            url,
            data,
            format="json",
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK,
        )
        self.assertIn("access", response.data)
