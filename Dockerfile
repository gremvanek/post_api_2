FROM python:3.12-slim

# Установите рабочий каталог
WORKDIR /app

# Скопируйте файлы
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .

# Команда по умолчанию
CMD ["gunicorn", "myproject.wsgi:application", "--bind", "0.0.0.0:8000"]
