# Dockerfile
FROM python:3-alpine

# Устанавливаем рабочую директорию
WORKDIR /usr/src/app

# Устанавливаем переменные окружения
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


RUN pip install --upgrade pip
# Копируем requirements.txt
COPY ./requirements.txt .

# Устанавливаем зависимости
RUN python3 -m pip install -r requirements.txt --no-cache-dir

# Копируем исходный код
COPY . .

# Применяем миграции
RUN python manage.py migrate

# Запускаем сервер разработки (для продакшена лучше использовать gunicorn или uWSGI)
CMD ["python", "app.py"]