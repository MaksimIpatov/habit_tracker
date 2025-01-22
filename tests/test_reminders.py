from unittest.mock import patch

from django.test import TestCase

from habits.models import Habit
from habits.tasks import send_habit_reminders
from users.models import User


class ReminderTaskTests(TestCase):
    def setUp(self) -> None:
        self.user = User.objects.create_user(
            email="reminder_user@mail.ru",
            password="password123",
            tg_chat_id="123456789",
        )
        self.habit = Habit.objects.create(
            user=self.user,
            action="Напоминание",
            place="Дом",
            time="10:00",
            execution_time=60,
            periodicity=1,
        )

    @patch("habits.tasks.send_notify_to_telegram")
    @patch("habits.tasks.send_mail")
    def test_send_habit_reminders(
        self,
        mock_send_mail,
        mock_send_telegram,
    ) -> None:
        send_habit_reminders()
        msg: str = (
            "Не забудьте выполнить привычку "
            "'Напоминание' в 10:00:00 в месте 'Дом'."
        )
        mock_send_telegram.assert_called_once_with(
            self.user.tg_chat_id,
            msg,
        )
        mock_send_mail.assert_called_once_with(
            subject="Напоминание о привычке: Напоминание",
            message=msg,
            from_email="noreply@habittracker.com",
            recipient_list=[self.user.email],
        )
