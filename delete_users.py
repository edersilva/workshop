import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app.settings')
django.setup()

from django.contrib.auth import get_user_model

User = get_user_model()
User.objects.filter(is_superuser=False).delete()
deleted, _ = User.objects.all().delete()
print(f"Deletados {deleted} usuários.")

