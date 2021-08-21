#!/bin/sh
source /opt/venv/bin/activate

echo "Static files. "
python manage.py collectstatic --noinput

echo "Making migrations and migrating the database. "
python manage.py migrate --noinput 

echo "Running server "
python manage.py runserver 5000

