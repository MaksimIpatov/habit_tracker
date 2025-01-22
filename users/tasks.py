from datetime import datetime, timedelta

from celery import shared_task
from django.utils import timezone

from users.constants import DEACTIVATE_ACCOUNTS_NUM_OF_DAYS
from users.models import User


@shared_task
def deactivate_inactive_users() -> None:
    threshold_date: datetime = timezone.now() - timedelta(
        days=DEACTIVATE_ACCOUNTS_NUM_OF_DAYS
    )
    User.objects.filter(
        last_login__lt=threshold_date,
        is_active=True,
    ).update(is_active=False)
