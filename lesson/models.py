from django.db import models
from professor.models import Professor
from django.utils.text import slugify
from faker import Faker
import random

class Lesson(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255, verbose_name="Aula")
    content = models.TextField(default="Nenhuma descrição definida", verbose_name="Descrição")
    short_description = models.TextField(default="Nenhuma descrição definida", verbose_name="Resumo")
    image = models.ImageField(upload_to='lessons/', null=True, blank=True, verbose_name="Imagem")
    video = models.TextField(verbose_name="Video")
    professor = models.ForeignKey(Professor, related_name='professor', on_delete=models.CASCADE, default=1, verbose_name="Professor")  # Or use an appropriate default
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    @classmethod
    def create_fake_lessons(cls, num_lessons=10):
        fake = Faker('pt_BR')
        professors = list(Professor.objects.all())
        
        for _ in range(num_lessons):
            lesson = cls(
                title=fake.sentence(nb_words=4),
                content=fake.paragraph(nb_sentences=5),
                short_description=fake.sentence(),
                video=f"https://www.youtube.com/watch?v={fake.lexify(text='?' * 11)}",
                professor=random.choice(professors)
            )
            lesson.save()
            
            # Optionally, set an image (you might want to handle this differently)
            # lesson.image.save(f"{slugify(lesson.title)}.jpg", ContentFile(get_random_image()), save=True)

    class Meta:
        verbose_name = 'Aula'
        verbose_name_plural = 'Aulas'
