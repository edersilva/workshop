from .models import JoinWorkshop, Workshop
from lesson.models import LessonCompleted

def is_user_joined(user, workshop):
    return JoinWorkshop.objects.filter(user=user, workshop=workshop).exists()

def has_user_completed_workshop(user, workshop):
    completed_lessons = LessonCompleted.objects.filter(user=user, workshop=workshop, lesson__in=workshop.lessons.all())
    return completed_lessons.values_list('lesson_id', flat=True)

def has_user_completed_all_lessons(user, workshop):
    total_lessons = workshop.lessons.count()
    completed_lessons = LessonCompleted.objects.filter(user=user, workshop=workshop, lesson__in=workshop.lessons.all()).count()
    return total_lessons == completed_lessons
