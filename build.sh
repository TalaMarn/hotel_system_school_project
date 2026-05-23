#!/bin/bash

# Exit on error
set -e

pip install -r requirements.txt

# Make migrations
echo "Making migrations..."
python manage.py makemigrations


# Apply database migrations
echo "Applying migrations..."
python manage.py migrate

# Collect static files
echo "Collecting static files..."
python manage.py collectstatic --noinput

echo "Build process completed successfully."
