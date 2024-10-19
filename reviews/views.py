from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Review
from django.contrib import messages
from workshops.models import Workshop  # Add this import

@login_required
def list_reviews(request):
    reviews = Review.objects.filter(user=request.user)
    context = {
        'reviews': reviews,
        'title': 'Comentários',
    }
    return render(request, 'reviews/list.html', context)

@login_required
def submit_review(request, workshop_id):
    workshop = get_object_or_404(Workshop, id=workshop_id)
    
    if request.method == 'POST':
        comment = request.POST.get('comment')
        rating = request.POST.get('rating')
        
        if comment and rating:
            Review.objects.create(
                user=request.user,
                workshop=workshop,
                comment=comment,
                rating=int(rating)
            )
            messages.success(request, 'Sua avaliação foi enviada com sucesso!')
            return redirect('workshop_detail', pk=workshop.id)
        else:
            messages.error(request, 'Por favor, preencha todos os campos.')
    
    return render(request, 'reviews/form.html', {'workshop': workshop})
