from django.apps import AppConfig


class LessonConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'lesson'
    verbose_name = 'Aulas'
    verbose_name_plural = 'Aula'