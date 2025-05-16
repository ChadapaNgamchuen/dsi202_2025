#!/bin/bash
set -e

# Set PYTHONPATH to include /usr/src/app/ to cover all apps
export PYTHONPATH=/usr/src/app:$PYTHONPATH

# Change to the directory where manage.py is located
cd /usr/src/app/myproject/myproject

# Run migrations
python manage.py migrate

# Start Django dev server
exec python manage.py runserver 0.0.0.0:8000