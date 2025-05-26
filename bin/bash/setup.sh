#!/bin/bash

set -e

echo "🚀 Running Django setup inside Docker..."

# Optional: Wait for database to be ready
# echo "⏳ Waiting for database..."
# until pg_isready -h "$DB_HOST" -p "$DB_PORT" -U "$DB_USER"; do
#   >&2 echo "Postgres is unavailable - sleeping"
#   sleep 1
# done
# echo "✅ Postgres is available."

# Migrate
echo "📦 Running migrations..."
python manage.py makemigrations
python manage.py migrate

# Collect static files
# echo "🧹 Collecting static files..."
# python manage.py collectstatic --noinput

echo "👤 Checking for superuser..."
echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.filter(is_superuser=True).exists()" \
  | python manage.py shell | grep -q "True"
if [ $? -ne 0 ]; then
    echo "⚙️ Creating superuser..."
    python manage.py shell <<EOF
    from django.contrib.auth import get_user_model
    User = get_user_model()
    if not User.objects.filter(username='admin').exists():
        User.objects.create_superuser(
            username='admin',
            email='admin@gmail.com',
            password='admin123',
            full_name='Admin User'
        )
    EOF
else
    echo "✅ Superuser already exists."
fi

# Start server
echo "🚀 Starting Django server..."
exec "$@"
