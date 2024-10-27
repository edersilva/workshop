from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.http import JsonResponse
from .models import Lesson, LessonCompleted
from workshops.models import Workshop, JoinWorkshop

def is_user_joined(user, workshop):
    return JoinWorkshop.objects.filter(user=user, workshop=workshop).exists()

def view_lesson(request, workshop_id, lesson_id):
    lesson = get_object_or_404(Lesson, id=lesson_id, workshops__id=workshop_id)
    workshop = get_object_or_404(Workshop, id=workshop_id)
    
    context = {
        'lesson': lesson,
        'is_completed': is_lesson_completed(request.user, lesson, workshop),
        'workshop': workshop,
        'workshop_title': workshop.title,
        'completed_lesson_ids': get_completed_lesson_ids(request.user, workshop),
        'joined': is_user_joined(request.user, workshop),
    }
    return render(request, 'lesson/view.html', context)

@require_POST
@login_required
def complete_lesson(request, workshop_id, lesson_id):
    try:
        lesson = get_object_or_404(Lesson, id=lesson_id)
        lesson_completed, created = LessonCompleted.objects.get_or_create(user=request.user, lesson=lesson, workshop_id=workshop_id)
        return JsonResponse({'success': True})
    except Lesson.DoesNotExist:
        return JsonResponse({'success': False, 'error': 'Lesson not found'}, status=404)
def is_lesson_completed(user, lesson, workshop):
    return LessonCompleted.objects.filter(user=user, lesson=lesson, workshop=workshop).exists()

def get_completed_lesson_ids(user, workshop):
    completed_lessons = LessonCompleted.objects.filter(user=user, workshop=workshop)
    return list(completed_lessons.values_list('lesson__id', flat=True))

