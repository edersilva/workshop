from django.contrib import admin
from .models import Workshop

class WorkshopAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'startdate', 'enddate')
    search_fields = ('title', 'description')
    list_filter = ('startdate', 'enddate')

admin.site.register(Workshop, WorkshopAdmin)