#!/bin/bash
migrate=$(python manage.py migrate | grep "No migrations to apply")

if [ -z "$migrate" ]
then
	python manage.py makemigrations
	python manage.py migrate
fi

gunicorn kindergarten.wsgi:application --bind 0.0.0.0:8000
