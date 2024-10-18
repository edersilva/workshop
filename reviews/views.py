from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Review

@login_required
def list_reviews(request):
    reviews = Review.objects.filter(user=request.user)
    context = {
        'reviews': reviews,
        'title': 'Comentários',
    }
    return render(request, 'reviews/list.html', context)