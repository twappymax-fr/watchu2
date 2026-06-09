#!/bin/sh

python manage.py collectstatic --noinput

echo "Running migrations"
python manage.py migrate



echo "Starting server..."
# Development
#python manage.py runserver 0.0.0.0:8000

# Deployment
python -m gunicorn watchu.wsgi:application --bind 0.0.0.0:8000 --workers 3