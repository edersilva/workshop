from django.core.management.base import BaseCommand
from django.utils.text import slugify
from lesson.models import Lesson
from professor.models import Professor
from faker import Faker
import random

class Command(BaseCommand):
    help = 'Populates the database with fake lessons'

    def handle(self, *args, **kwargs):
        fake = Faker('pt_BR')
        professors = list(Professor.objects.all())
        
        if not professors:
            self.stdout.write(self.style.ERROR('No professors found. Please create professors first.'))
            return

        for _ in range(10):  # Create up to 10 lessons
            lesson = Lesson(
                title=fake.sentence(nb_words=4),
                content=fake.paragraph(nb_sentences=5),
                short_description=fake.sentence(),
                video=f"https://www.youtube.com/watch?v={fake.lexify(text='?' * 11)}",
                professor=random.choice(professors)
            )
            lesson.save()
            
            self.stdout.write(self.style.SUCCESS(f'Created lesson: {lesson.title}'))

        self.stdout.write(self.style.SUCCESS('Successfully populated lessons'))