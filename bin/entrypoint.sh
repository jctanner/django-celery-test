#!/bin/bash

set -e

cd /code/django_celery_test

python manage.py makemigrations
python manage.py migrate

python manage.py create_superuser

python manage.py runserver 0.0.0.0:8000

