from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

class Category(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255, verbose_name="Título")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Categorias'
        verbose_name_plural = 'Categorias'

class Workshop(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255, verbose_name="Título")
    image = models.ImageField(upload_to='workshops/', null=True, blank=True, verbose_name="Imagem")
    description = models.TextField(default="Nenhuma descrição definida", verbose_name="Descrição")
    short_description = models.TextField(default="Nenhuma descrição definida", verbose_name="Resumo")
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='categories', null=True, blank=True, verbose_name="Categoria")
    startdate = models.DateTimeField(verbose_name="Data de início")
    enddate = models.DateTimeField(verbose_name="Data de término")
    lessons = models.ManyToManyField('lesson.Lesson', related_name='workshops', verbose_name="Aulas do workshop")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.title

class WorkshopFavorite(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='workshop_favorites')
    workshop = models.ForeignKey('Workshop', on_delete=models.CASCADE, related_name='favorites')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'workshop')

class JoinWorkshop(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='join_workshops')
    workshop = models.ForeignKey('Workshop', on_delete=models.CASCADE, related_name='join_workshops')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Inscritos'
        verbose_name_plural = 'Inscritos'
        unique_together = ('user', 'workshop')
