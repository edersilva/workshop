from django.contrib import admin
from .models import Lesson

class LessonAdmin(admin.ModelAdmin):
    list_display = ('title', 'short_description', 'video', 'professor')
    search_fields = ('title', 'description', 'short_description')
    list_filter = ('professor',)
    
    # Adicione estas linhas
    verbose_name = 'Aula'
    verbose_name_plural = 'Aulas'

admin.site.register(Lesson, LessonAdmin)