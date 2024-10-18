from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

class Review(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, verbose_name="Usuário")
    workshop = models.ForeignKey('workshops.Workshop', on_delete=models.PROTECT)
    RATING_CHOICES = [(i, str(i)) for i in range(1, 6)]
    rating = models.IntegerField(
        choices=RATING_CHOICES,
        validators=[MinValueValidator(1), MaxValueValidator(5)],
        verbose_name="Avaliação"
    )
    comment = models.TextField(verbose_name="Comentário")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Comentário'
        verbose_name_plural = 'Comentários'