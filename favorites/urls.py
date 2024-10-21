from django.urls import path
from . import views

app_name = 'favorites'

urlpatterns = [
    path('favorites/', views.list_favorites, name='list_favorites'),
    path('favorites/delete/<int:favorite_id>/', views.delete_favorite, name='delete_favorite'),
    path('favorites/add/<int:workshop_id>/', views.favorite, name='favorite'),
]

