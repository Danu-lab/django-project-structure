#!/bin/bash
set -e

# echo "Waiting for PostgreSQL..."
# while ! nc -z db 5432; do
#   sleep 1
# done
# echo "PostgreSQL is up!"

# echo "Waiting for Redis..."
# while ! nc -z redis 6379; do
#   sleep 1
# done
# echo "Redis is up!"

# echo "Running migrations..."
# python manage.py migrate

echo "Starting server..."
exec uv run manage.py runserver 0.0.0.0:8000
