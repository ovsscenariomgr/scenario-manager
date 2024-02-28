#!/bin/bash

# Apply database migrations
echo "Apply database migrations"
python manage.py migrate --noinput

# Apply fixtures
echo "Apply fixtures"
python manage.py loaddata users

# Collect static files
echo "Collect static files"
python manage.py collectstatic --noinput

# Start server
# echo "Starting server"
# python manage.py runserver 0.0.0.0:8000
exec "$@"