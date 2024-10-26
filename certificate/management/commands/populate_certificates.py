import os
import django
import random
from faker import Faker
from django.core.management.base import BaseCommand

# Configurar o ambiente Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'your_project_name.settings')
django.setup()

from django.contrib.auth import get_user_model
from certificate.models import Certificate
from workshops.models import Workshop

fake = Faker()

class Command(BaseCommand):
    help = 'Populates the database with fake certificates'

    def add_arguments(self, parser):
        parser.add_argument('count', nargs='?', type=int, default=10, help='Number of certificates to create')

    def handle(self, *args, **options):
        count = options['count']
        self.create_fake_certificates(count)

    def create_fake_certificates(self, count):
        User = get_user_model()
        users = User.objects.all()
        certificates = Certificate.objects.all()
        workshops = Workshop.objects.all()

        if not users or not workshops:
            self.stdout.write(self.style.WARNING("Certifique-se de que existem usuários e workshops no banco de dados."))
            return

        for _ in range(count):
            user = random.choice(users)
            certificate = random.choice(certificates)
            workshop = random.choice(workshops)
            
            # Verifica se o favorito já existe para evitar duplicatas
            if not Certificate.objects.filter(user=user, workshop=workshop).exists():
                Certificate.objects.create(user=user, workshop=workshop)
                self.stdout.write(self.style.SUCCESS(f"Favorito criado: Usuário {user.username} - Workshop {workshop.title}"))
            else:
                self.stdout.write(self.style.WARNING(f"Favorito já existe: Usuário {user.username} - Workshop {workshop.title}"))
