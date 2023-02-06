#!/bin/sh

python manage.py migrate

# Outros comandos como loaddata, collectstatic, etc.

exec "$@"
