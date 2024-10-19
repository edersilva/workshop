import os
import django
import random
from faker import Faker

# Configurar o ambiente Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'your_project_name.settings')
django.setup()

from django.contrib.auth import get_user_model
from favorites.models import Favorite
from workshops.models import Workshop

fake = Faker()

def create_fake_favorites():
    User = get_user_model()
    users = User.objects.all()
    workshops = Workshop.objects.all()

    if not users or not workshops:
        print("Certifique-se de que existem usuários e workshops no banco de dados.")
        return

    for _ in range(10):
        user = random.choice(users)
        workshop = random.choice(workshops)
        
        # Verifica se o favorito já existe para evitar duplicatas
        if not Favorite.objects.filter(user=user, workshop=workshop).exists():
            Favorite.objects.create(user=user, workshop=workshop)
            print(f"Favorito criado: Usuário {user.username} - Workshop {workshop.title}")
        else:
            print(f"Favorito já existe: Usuário {user.username} - Workshop {workshop.title}")

if __name__ == '__main__':
    create_fake_favorites()
