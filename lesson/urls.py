from django.urls import path
from . import views

app_name = 'lesson'

urlpatterns = [
    path('workshops/<int:workshop_id>/<int:lesson_id>/', views.view_lesson, name='view_lesson'),
    path('lesson/complete/<int:workshop_id>/<int:lesson_id>/', views.complete_lesson, name='complete_lesson'),
]
