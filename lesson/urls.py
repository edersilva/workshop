from django.urls import path
from . import views

app_name = 'lesson'  # Add this line

urlpatterns = [
    path('workshops/<int:workshop_id>/<int:lesson_id>/', views.view_lesson, name='view_lesson'),
]
