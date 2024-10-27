#!/bin/bash

# Aguarde o banco de dados iniciar (opcional, para uso com Docker Compose)
# sleep 5

# Realize as migrações
python manage.py makemigrations
python manage.py migrate
python manage.py populate_professors 10
python manage.py populate_lessons 10
python manage.py populate_workshops 20
python manage.py populate_users 10
python manage.py populate_favorites 10
python manage.py populate_reviews 10
python manage.py populate_certificates 10

# Crie o superusuário automaticamente, se ele ainda não existir
python manage.py shell <<EOF
from django.contrib.auth import get_user_model
User = get_user_model()
if not User.objects.filter(username='pucminas').exists():
    User.objects.create_superuser('pucminas', 'puc@minas.com', 'admin123')
EOF

# Inicie o servidor Django
exec python manage.py runserver 0.0.0.0:8000