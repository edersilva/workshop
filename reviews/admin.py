from django.contrib import admin
from .models import Review

class ReviewAdmin(admin.ModelAdmin):
    list_display = ('user', 'workshop', 'comment', 'rating', 'created_at')
    list_filter = ('workshop', 'rating')
    search_fields = ('user__username', 'workshop__title', 'comment')

admin.site.register(Review, ReviewAdmin)