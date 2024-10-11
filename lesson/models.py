from django.db import models
from professor.models import Professor
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