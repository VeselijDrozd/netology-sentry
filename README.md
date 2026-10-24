# Домашнее задание: Платформа мониторинга Sentry

Решение к занятию 16 «Платформа мониторинга Sentry».

---

## Задание 1. Free Cloud account

Создан бесплатный аккаунт на [sentry.io](https://sentry.io) через GitHub.

**Скриншот меню Projects:**

![Projects](screenshots/01-projects.png)

---

## Задание 2. Sample event и Resolved

1. Создан Python-проект в Sentry.
2. Сгенерировано тестовое событие через `Generate sample event`.
3. Событие изучено и помечено как `Resolved`.

**Скриншот Stack trace:**

![Stack trace](screenshots/02-stack-trace.png)

**Список событий после Resolved:**

![Issues after Resolved](screenshots/02-issues-resolved.png)

---

## Задание 3. Правила алёртинга

1. Создано дефолтное правило алёртинга (все поля — `all`).
2. Снова сгенерировано `Generate sample event`.
3. На почту, привязанную к GitHub-аккаунту, пришло оповещение.

**Скриншот тела письма:**

![Alert email](screenshots/03-alert-email.png)

---

## Задание повышенной сложности. Sentry SDK

Небольшое Python-приложение подключает [sentry-sdk](https://docs.sentry.io/platforms/python/) и отправляет несколько тестовых событий.

### Запуск

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

cp .env.example .env   # если .env ещё нет
# откройте .env и вставьте свой DSN

python app.py
```

DSN: **Settings → Projects → [ваш проект] → Client Keys (DSN)**.  
Файл `.env` в `.gitignore` и в репозиторий не попадает; в git только `.env.example`.

### Код

См. [`app.py`](app.py).
