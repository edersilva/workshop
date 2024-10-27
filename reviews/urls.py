from django.urls import path
from . import views

app_name = 'reviews'

urlpatterns = [
    path('comments/', views.view_reviews, name='view_reviews'),
    path('submit/<int:workshop_id>/', views.submit_review, name='submit_review'),
    path('delete/<int:review_id>/', views.delete_review, name='delete_review'),
]

