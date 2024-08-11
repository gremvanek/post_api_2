# Используем базовый образ Python
FROM python:3.12-slim

# Устанавливаем переменную окружения, которая гарантирует, что вывод из python
# будет отправлен прямо в терминал без предварительной буферизации
ENV PYTHONUNBUFFERED 1

# Устанавливаем рабочую директорию в контейнере
WORKDIR /app

# Устанавливаем virtualenv
RUN pip install --upgrade pip \
    && pip install virtualenv

# Создаем виртуальное окружение
RUN python -m venv /venv

# Активируем виртуальное окружение
ENV PATH="/venv/bin:$PATH"

# Копируем файл requirements.txt в рабочую директорию
COPY requirements.txt /app/

# Устанавливаем зависимости в виртуальное окружение
RUN pip install -r requirements.txt

# Копируем остальные файлы проекта
COPY . /app/

# Команда для запуска Django-сервера
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
