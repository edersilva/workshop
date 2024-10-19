from django.core.management.base import BaseCommand
from professor.models import Professor
from faker import Faker
import random

class Command(BaseCommand):
    help = 'Populate the database with fake professors'

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='Number of professors to create')

    def handle(self, *args, **kwargs):
        fake = Faker('pt_BR')
        count = kwargs['count']

        for _ in range(count):
            Professor.objects.create(
                title=f"Prof. Dr. {fake.name()}",
                email=fake.email(),
                description=fake.text(max_nb_chars=500),
                # Note: Faker doesn't generate actual image files, so we'll leave it blank
            )

        self.stdout.write(self.style.SUCCESS(f'Successfully created {count} professors'))

