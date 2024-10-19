from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from workshops.models import Workshop
from reviews.models import Review
from django.utils import timezone
import random

User = get_user_model()

class Command(BaseCommand):
    help = 'Populates the database with fake reviews'

    def add_arguments(self, parser):
        parser.add_argument('count', nargs='?', type=int, default=10, help='Number of reviews to create')

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
            
            review, created = Review.objects.get_or_create(
                user=user,
                workshop=workshop,
                defaults={
                    'rating': random.randint(1, 5),
                    'comment': f'This is a sample comment for {workshop.title}. It was great!',
                    'created_at': timezone.now(),
                    'updated_at': timezone.now(),
                }
            )

            if created:
                self.stdout.write(self.style.SUCCESS(f'Review criado: {user.username} - {workshop.title} - Rating: {review.rating}'))
            else:
                self.stdout.write(self.style.WARNING(f'Review já existia: {user.username} - {workshop.title}'))

        self.stdout.write(self.style.SUCCESS(f'Processo de população de {count} reviews concluído.'))