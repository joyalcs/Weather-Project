FROM python:3.12
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
WORKDIR /weather_backend
COPY requirements.txt /weather_backend/
RUN pip install --upgrade pip && pip install -r requirements.txt
COPY . .
EXPOSE 8000
# CMD ["sh", "-c", "python manage.py wait_for_db && python manage.py makemigrations && python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]