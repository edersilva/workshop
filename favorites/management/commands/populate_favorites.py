from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from workshops.models import Workshop
from favorites.models import Favorite
from django.utils import timezone
import random

User = get_user_model()

class Command(BaseCommand):
    help = 'Populates the database with fake favorites'

    def add_arguments(self, parser):
        parser.add_argument('count', nargs='?', type=int, default=10, help='Number of favorites to create')

    def handle(self, *args, **options):
        count = options['count']
        users = User.objects.all()
        workshops = Workshop.objects.all()

        if not users or not workshops:
            self.stdout.write(self.style.ERROR('Certifique-se de que existem usuários e workshops no banco de dados.'))
            return

        for _ in range(count):
            user = random.choice(users)
            workshop = random.choice(workshops)
            
            favorite, created = Favorite.objects.get_or_create(
                user=user,
                workshop=workshop,
                defaults={
                    'created_at': timezone.now(),
                    'updated_at': timezone.now(),
                }
            )

            if created:
                self.stdout.write(self.style.SUCCESS(f'Favorito criado: {user.username} - {workshop.title}'))
            else:
                self.stdout.write(self.style.WARNING(f'Favorito já existia: {user.username} - {workshop.title}'))

        self.stdout.write(self.style.SUCCESS(f'Processo de população de {count} favoritos concluído.'))
