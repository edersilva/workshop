from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Workshop, Category, JoinWorkshop

class WorkshopAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'startdate', 'enddate')
    search_fields = ('title', 'description')
    list_filter = ('startdate', 'enddate')

class CategoriesAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)

class JoinWorkshopAdmin(admin.ModelAdmin):
    list_display = ('user', 'workshop')
    search_fields = ('user__first_name', 'workshop__title')

admin.site.register(Workshop, WorkshopAdmin)
admin.site.register(Category, CategoriesAdmin)
admin.site.register(JoinWorkshop, JoinWorkshopAdmin)
