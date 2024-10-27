from django.db import models
from professor.models import Professor
from workshops.models import Workshop
from django.contrib.auth.models import User
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

    class Meta:
        verbose_name = 'Aula'
        verbose_name_plural = 'Aulas'

class LessonCompleted(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    workshop = models.ForeignKey(Workshop, on_delete=models.CASCADE)
    completed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.lesson.title}"
