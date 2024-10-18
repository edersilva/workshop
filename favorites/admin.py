from django.contrib import admin
from .models import Favorite

class FavoriteAdmin(admin.ModelAdmin):
    list_display = ('user', 'workshop', 'created_at')
    list_filter = ('user', 'workshop')
    search_fields = ('user__username', 'workshop__name')

admin.site.register(Favorite, FavoriteAdmin)

