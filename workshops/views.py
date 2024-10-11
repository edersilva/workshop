from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from django.db.models import Avg
from .models import Workshop

class WorkshopListView(ListView):
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
        return context

class WorkshopDetailView(DetailView):
    model = Workshop
    template_name = 'workshops/view.html'
    context_object_name = 'workshop'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.object.title
        return context

def view_workshop(request, workshop_id):
    workshop = get_object_or_404(Workshop, id=workshop_id)
    context = {
        'workshop': workshop,
        'workshop_title': workshop.title,
    }
    return render(request, 'workshop/view.html', context)
