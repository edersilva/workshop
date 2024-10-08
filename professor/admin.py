from django.contrib import admin
from .models import Professor

class ProfessorAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'email')
    search_fields = ('title', 'description', 'email')

admin.site.register(Professor, ProfessorAdmin)
