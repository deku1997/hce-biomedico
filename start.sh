#!/bin/bash
python manage.py migrate --noinput
python manage.py collectstatic --noinput
gunicorn hce_project.wsgi:application
