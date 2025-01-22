# Habit Tracker

---

## Описание проекта

**Habit Tracker** - это веб-сервис для отслеживания привычек, который помогает пользователям:

- создавать
- управлять
- отслеживать выполнение как полезных, так и приятных привычек.

Проект поддерживает интеграцию с Telegram для отправки напоминаний о запланированных привычках.

---

## Стек технологий:

- Python 3
- Django 4
- Django REST Framework (DRF)
- PostgreSQL
- Celery + Redis
- Telegram API
- coverage

---

## Как запустить проект

Шаги для локального запуска проекта:

1. **Клонировать репозиторий и перейти в директорию проекта:**

    ```bash
    git clone https://github.com/MaksimIpatov/habit_tracker.git && cd habit_tracker
    ```

2. **Создать виртуальное окружение и активировать его:**

    - **Windows**:

      ```bash
      python -m venv .venv
      .venv\Scripts\activate
      ```

    - **MacOS/Linux**:

      ```bash
      python3 -m venv .venv
      source .venv/bin/activate
      ```

3. **Установить зависимости:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Настроить переменные окружения:**

    - Создайте файл `.env` и добавьте туда параметры из `.env.sample`.

5. **Применить миграции базы данных:**

    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

6. **Запустить сервер:**

    ```bash
    python manage.py runserver
    ```

   Сервис будет доступен по адресу: http://127.0.0.1:8000/

---

## Эндпоинты API

1. **Привычки:**

    - `GET /api/habits/` - получить список привычек текущего пользователя
    - `GET /api/habits/?public=1` - получить список публичных привычек
    - `GET /api/habits/{id}/` - получить информацию о привычке
    - `POST /api/habits/` - создать новую привычку
    - `PUT /api/habits/{id}/` - обновить привычку
    - `DELETE /api/habits/{id}/` - удалить привычку

2. **Пользователи:**

    - `POST /users/register/` - регистрация нового пользователя
    - `POST /users/login/` - авторизация пользователя
    - `GET /users/{id}/` - получить информацию о пользователе
    - `PUT /users/{id}/edit/` - обновить информацию о пользователе
    - `DELETE /users/{id}/delete/` - удалить пользователя

---

## Запуск тестов

- Проверьте статус тестового покрытия проекта:

```bash
coverage report
```

- Для запуска тестов, из корня проекта запустить команду:

```bash
coverage run --source='.' manage.py test
```

## Запуск фоновых задач

Запустить задачи Celery:

```bash
celery -A habit_tracker worker -l INFO
```

Запустить периодические задачи Celery:

```bash
celery -A habit_tracker beat -l INFO
```
