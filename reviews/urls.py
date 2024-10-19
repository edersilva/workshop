from django.urls import path
from . import views

app_name = 'reviews'

urlpatterns = [
    path('', views.list_reviews, name='list_reviews'),
    path('submit/<int:workshop_id>/', views.submit_review, name='submit_review'),
]

