from celery import shared_task
from django.core.mail import send_mail

from habits.models import Habit
from habits.services import send_notify_to_telegram


@shared_task
def send_habit_reminders() -> None:
    habits = Habit.objects.filter(periodicity__gte=1)

    for habit in habits:
        msg_title: str = f"Напоминание о привычке: {habit.action}"
        msg: str = (
            f"Не забудьте выполнить привычку '{habit.action}' "
            f"в {habit.time} в месте '{habit.place}'."
        )
        if habit.user.tg_chat_id:
            send_notify_to_telegram(habit.user.tg_chat_id, msg)

        send_mail(
            subject=msg_title,
            message=msg,
            from_email="noreply@habittracker.com",
            recipient_list=[habit.user.email],
        )
