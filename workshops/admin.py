from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Workshop, Category, JoinWorkshop

class WorkshopAdmin(admin.ModelAdmin):
    list_display = ('image_preview', 'title', 'description', 'startdate', 'enddate')
    search_fields = ('title', 'description')
    list_filter = ('startdate', 'enddate')

    def image_preview(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" width="50" height="50" />')
        return mark_safe(f'<img src="{obj.placeholder_image}" width="50" height="50" />')
    image_preview.allow_tags = True
    image_preview.short_description = 'Imagem'


class CategoriesAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)

class JoinWorkshopAdmin(admin.ModelAdmin):
    list_display = ('user', 'workshop')
    search_fields = ('user__first_name', 'workshop__title')

admin.site.register(Workshop, WorkshopAdmin)
admin.site.register(Category, CategoriesAdmin)
admin.site.register(JoinWorkshop, JoinWorkshopAdmin)
