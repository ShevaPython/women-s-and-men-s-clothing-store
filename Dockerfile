# Используем минимальный базовый образ Python
FROM python:3.10-slim

# Установка инструмента Poetry
RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/install-poetry.py | python3 -

# Добавление файла pyproject.toml и lock-файла poetry.lock
COPY pyproject.toml poetry.lock* /app/

# Устанавливаем зависимости с помощью Poetry
WORKDIR /app
RUN poetry config virtualenvs.create false && poetry install --no-dev --no-root

# Копируем остальные файлы проекта в контейнер
COPY . /app

# Определяем команду для запуска приложения
CMD ["poetry", "run", "python", "manage.py", "runserver", "0.0.0.0:8000"]
