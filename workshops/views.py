from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from django.db.models import Avg, Count
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Workshop, JoinWorkshop
from lesson.models import LessonCompleted, Lesson

class WorkshopListView(LoginRequiredMixin, ListView):
    model = Workshop
    template_name = 'workshops/list.html'
    context_object_name = 'workshops'

    def get_queryset(self):
        return Workshop.objects.annotate(
            avg_rating=Avg('review__rating')
        ).order_by('-startdate')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Workshops'
        
        # Get the workshops the user has joined
        user_joined_workshops = JoinWorkshop.objects.filter(user=self.request.user).values_list('workshop_id', flat=True)
        context['user_joined'] = user_joined_workshops
        
        return context

class WorkshopAccountListView(LoginRequiredMixin, ListView):
    model = Workshop
    template_name = 'workshops/account_list.html'
    context_object_name = 'workshops'

    def get_queryset(self):
        return Workshop.objects.annotate(
            avg_rating=Avg('review__rating')
        ).order_by('-startdate')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Meus Workshops'
        
        # Get the workshops the user has joined
        user_joined_workshops = JoinWorkshop.objects.filter(user=self.request.user).values_list('workshop_id', flat=True)
        context['user_joined'] = user_joined_workshops
        
        return context

class WorkshopDetailView(DetailView):
    model = Workshop
    template_name = 'workshops/view.html'
    context_object_name = 'workshop'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.object.title
        context['reviews'] = self.object.review_set.all()
        context['is_joined'] = is_user_joined(self.request.user, self.object)
        context['status'] = has_user_completed_workshop(self.request.user, self.object)
        return context

def view_workshop(request, workshop_id):
    workshop = get_object_or_404(Workshop, id=workshop_id)
    context = {
        'workshop': workshop,
        'workshop_title': workshop.title,
    }
    return render(request, 'workshop/view.html', context)

@require_POST
@login_required
def join_workshop(request, workshop_id):
    try:
        workshop = Workshop.objects.get(id=workshop_id)
        join, created = JoinWorkshop.objects.get_or_create(user=request.user, workshop=workshop)
        return JsonResponse({'success': True})
    except Workshop.DoesNotExist:
        return JsonResponse({'success': False, 'error': 'Workshop not found'}, status=404)

def is_user_joined(user, workshop):
    return JoinWorkshop.objects.filter(user=user, workshop=workshop).exists()

def has_user_completed_workshop(user, workshop):
    total_lessons = workshop.lessons.count()
    completed_lessons = LessonCompleted.objects.filter(user=user, workshop=workshop, lesson__in=workshop.lessons.all())
    return completed_lessons.values_list('lesson_id', flat=True)
