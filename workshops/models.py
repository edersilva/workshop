from django.db import models

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