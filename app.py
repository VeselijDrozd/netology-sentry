"""Минимальный пример отправки событий в Sentry через SDK."""

import os
import sys

from dotenv import load_dotenv
import sentry_sdk
from sentry_sdk import capture_exception, capture_message, set_tag, set_user

load_dotenv()

dsn = os.environ.get("SENTRY_DSN")
if not dsn:
    print(
        "Задайте SENTRY_DSN в файле .env (см. .env.example) "
        "или в переменной окружения.",
        file=sys.stderr,
    )
    sys.exit(1)

sentry_sdk.init(
    dsn=dsn,
    environment="homework",
    release="netology-sentry@1.0.0",
    traces_sample_rate=1.0,
)

set_user({"id": "student-1", "username": "netology-student"})
set_tag("homework", "10-monitoring-05-sentry")

capture_message("Тестовое сообщение из homework app", level="info")
capture_message("Предупреждение: демо warning-событие", level="warning")

try:
    _ = 1 / 0
except ZeroDivisionError as exc:
    capture_exception(exc)

print("События отправлены в Sentry. Проверьте Issues в UI.")
