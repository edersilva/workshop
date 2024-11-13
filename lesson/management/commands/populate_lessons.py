from django.core.management.base import BaseCommand
from django.utils.text import slugify
from lesson.models import Lesson
from professor.models import Professor
from faker import Faker
import random

class Command(BaseCommand):
    help = 'Populates the database with fake lessons'

    def add_arguments(self, parser):
        parser.add_argument('count', nargs='?', type=int, default=10, help='Number of lessons to create')

    def handle(self, *args, **options):
        fake = Faker('pt_BR')
        professors = list(Professor.objects.all())
        count = options['count']
        
        if not professors:
            self.stdout.write(self.style.ERROR('Nenhum professor encontrado. Por favor, crie professores primeiro.'))
            return

        for _ in range(count):  # Create the specified number of lessons
            lesson = Lesson(
                title=fake.sentence(nb_words=4).rstrip('.'),
                content='\n'.join([fake.paragraph(nb_sentences=3) for _ in range(3)]),
                short_description=fake.text(max_nb_chars=100).rstrip('.'),
                video=f"https://www.youtube.com/watch?v={fake.lexify(text='?' * 11)}",
                professor=random.choice(professors)
            )
            lesson.save()
            
            self.stdout.write(self.style.SUCCESS(f'Aula criada: {lesson.title}'))

        self.stdout.write(self.style.SUCCESS(f'População concluída com sucesso: {count} aulas criadas'))
