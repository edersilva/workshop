from django.contrib import admin
from .models import Lesson, LessonCompleted

class LessonAdmin(admin.ModelAdmin):
    list_display = ('title', 'short_description', 'video', 'professor')
    search_fields = ('title', 'description', 'short_description')
    list_filter = ('professor',)
    
    verbose_name = 'Aula'
    verbose_name_plural = 'Aulas'

class LessonCompletedAdmin(admin.ModelAdmin):
    list_display = ('user', 'lesson', 'workshop', 'completed_at')
    search_fields = ('user__username', 'lesson__title', 'workshop__title')
    list_filter = ('workshop',)

    verbose_name = 'Aula Concluída'
    verbose_name_plural = 'Aulas Concluídas'

admin.site.register(Lesson, LessonAdmin)
admin.site.register(LessonCompleted, LessonCompletedAdmin)
