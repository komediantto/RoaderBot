#!/bin/bash

cd app

# Запуск миграций Django
python manage.py makemigrations
python manage.py migrate

python manage.py runserver 0.0.0.0:8000

