from django.apps import AppConfig


class ProfessorConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'professor'
    verbose_name = 'Professores'
    verbose_name_plural = 'Professores'