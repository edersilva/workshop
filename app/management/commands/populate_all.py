from django.core.management.base import BaseCommand
from django.core.management import call_command

class Command(BaseCommand):
    help = 'Populate the database with sample data'

    def handle(self, *args, **kwargs):
        self.stdout.write('Starting database population...')

        call_command('populate_professors', 10)
        call_command('populate_lessons', 10)
        call_command('populate_workshops', 20)
        call_command('populate_users', 10)
        call_command('populate_favorites', 10)
        call_command('populate_certificates', 10)

        self.stdout.write(self.style.SUCCESS('Database population completed successfully!'))