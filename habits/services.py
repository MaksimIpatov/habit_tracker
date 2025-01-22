import requests
from django.conf import settings


def send_notify_to_telegram(chat_id: str, msg: str) -> None:
    params: dict[str, str] = {
        "text": msg,
        "chat_id": chat_id,
    }
    try:
        response = requests.get(
            f"{settings.TELEGRAM_API_URL}",
            params=params,
        )
        print(f"Статус отправки: {response.status_code}")
    except requests.RequestException as err_msg:
        print(f"Ошибка при отправке уведомлений в Телеграм: {err_msg}")
