from django.shortcuts import render, get_object_or_404
from .models import Lesson
from workshops.models import Workshop

def view_lesson(request, workshop_id, lesson_id):
    lesson = get_object_or_404(Lesson, id=lesson_id, workshops__id=workshop_id)
    workshop = get_object_or_404(Workshop, id=workshop_id)
    
    context = {
        'lesson': lesson,
        'workshop': workshop,
        'workshop_title': workshop.title,
    }
    return render(request, 'lesson/view.html', context)
