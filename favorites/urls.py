from django.urls import path
from . import views

app_name = 'favorites'

urlpatterns = [
    path('favorites/', views.list_favorites, name='list_favorites'),
    path('api/favorites/<int:favorite_id>/', views.delete_favorite, name='delete_favorite'),
]

