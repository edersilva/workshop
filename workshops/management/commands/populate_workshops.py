from django.core.management.base import BaseCommand
from django.utils import timezone
from workshops.models import Workshop, Category
from lesson.models import Lesson
from faker import Faker
import factory
import random

fake = Faker('pt_BR')

class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Category

    title = factory.LazyFunction(lambda: fake.unique.word().capitalize())

class WorkshopFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Workshop

    title = factory.LazyFunction(lambda: fake.sentence(nb_words=4))
    description = factory.LazyFunction(lambda: fake.paragraph(nb_sentences=3))
    short_description = factory.LazyFunction(lambda: fake.sentence(nb_words=10))
    startdate = factory.LazyFunction(lambda: fake.date_time_between(start_date='+1d', end_date='+30d'))
    enddate = factory.LazyFunction(lambda: fake.date_time_between(start_date='+31d', end_date='+60d'))
    image = factory.LazyFunction(lambda: fake.image_url())

    @factory.post_generation
    def category(self, create, extracted, **kwargs):
        if not create:
            return

        available_categories = list(Category.objects.all())
        num_categories = random.randint(1, min(2, len(available_categories)))
        selected_category = random.choice(available_categories)
        self.category = selected_category

    @factory.post_generation
    def lessons(self, create, extracted, **kwargs):
        if not create:
            return

        available_lessons = list(Lesson.objects.all())
        num_lessons = min(5, len(available_lessons))
        selected_lessons = random.sample(available_lessons, num_lessons)
        self.lessons.add(*selected_lessons)

class Command(BaseCommand):
    help = 'Creates up to 10 fake workshops with associated lessons and up to 5 categories'

    def handle(self, *args, **options):
        # Create categories
        num_categories = random.randint(1, 5)
        for _ in range(num_categories):
            category = CategoryFactory()
            self.stdout.write(self.style.SUCCESS(f'Created category: {category.title}'))

        if Lesson.objects.count() == 0:
            self.stdout.write(self.style.WARNING('No lessons found. Please create some lessons first.'))
            return

        # Create workshops
        num_workshops = random.randint(5, 10)
        for _ in range(num_workshops):
            workshop = WorkshopFactory()
            self.stdout.write(self.style.SUCCESS(f'Created workshop: {workshop.title}'))

        self.stdout.write(self.style.SUCCESS(f'Successfully created {num_workshops} fake workshops with associated lessons and {num_categories} categories'))
