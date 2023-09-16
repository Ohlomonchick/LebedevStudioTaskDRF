#!/bin/bash

cd /app/

source /opt/venv/bin/activate

SUPERUSER_NAME=${DJANGO_SUPERUSER_USERNAME:-"admin"}
SUPERUSER_EMAIL=${DJANGO_SUPERUSER_EMAIL:-"default@email.com"}

cd /app/

python manage.py makemigrations --noinput
python manage.py migrate --noinput
python manage.py flush --noinput
python manage.py createsuperuser --username "$SUPERUSER_NAME" --email "$SUPERUSER_EMAIL" --noinput || true

python parser.py
python manage.py runserver 0.0.0.0:8000