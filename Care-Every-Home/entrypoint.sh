#!/bin/bash

# รอ DB ให้พร้อมก่อน (optional)
# echo "Waiting for PostgreSQL..."
# sleep 5

# Apply database migrations
python manage.py migrate

# Collect static files (ถ้ามี)
# python manage.py collectstatic --noinput

# Run server
exec "$@"
