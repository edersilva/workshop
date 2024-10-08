from django.db import models

class Professor(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255, verbose_name="Professor")
    email = models.EmailField(max_length=255, verbose_name="Email")
    description = models.TextField(default="Nenhuma descrição definida", verbose_name="Biografia")
    image = models.ImageField(upload_to='professors/', null=True, blank=True, verbose_name="Imagem")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    class Meta:
        verbose_name = 'Professor'
        verbose_name_plural = 'Professores'