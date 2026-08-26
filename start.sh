#!/bin/bash
echo "=== Iniciando despliegue en Railway ==="
echo "Ejecutando migraciones..."
python manage.py migrate --noinput
echo "Recolectando archivos estáticos..."
python manage.py collectstatic --noinput
echo "Iniciando servidor Gunicorn..."
gunicorn hce_project.wsgi:application