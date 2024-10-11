from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView
from .models import Review

class ReviewListView(ListView):
    model = Review
    template_name = 'reviews/list.html'
    context_object_name = 'reviews'

    def get_queryset(self):
        return Review.objects.select_related('user', 'workshop').order_by('-created_at')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['reviews_data'] = {
            'title': 'Comentários',
            'reviews': context['reviews'],
            'teste': 'Valor de teste'
        }
        return context
