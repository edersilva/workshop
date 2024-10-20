from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Review
from django.contrib import messages
from workshops.models import Workshop
from django.views.decorators.http import require_http_methods
from django.http import JsonResponse
import logging

logger = logging.getLogger(__name__)

@login_required
def list_reviews(request):
    reviews = Review.objects.filter(user=request.user)
    context = {
        'reviews': reviews,
        'title': 'Comentários',
    }
    return render(request, 'reviews/list.html', context)

@login_required
def view_reviews(request):
    reviews = Review.objects.filter(user=request.user)
    context = {
        'reviews': reviews,
        'title': 'Comentários',
    }
    return render(request, 'reviews/view.html', context)

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

@login_required
@require_http_methods(["DELETE"])
def delete_review(request, review_id):
    try:
        review = Review.objects.get(id=review_id, user=request.user)
        review.delete()
        logger.info(f"Comentário {review_id} deletado com sucesso.")
        return JsonResponse({'message': 'Comentário deletado com sucesso.'}, status=200)
    except Review.DoesNotExist:
        logger.warning(f"Tentativa de deletar comentário inexistente ou não pertencente ao usuário. ID: {review_id}, Usuário: {request.user.id}")
        return JsonResponse({'error': 'Comentário não encontrado ou não pertence ao usuário atual.'}, status=404)
    except Exception as e:
        logger.error(f"Erro ao deletar comentário {review_id}: {str(e)}")
        return JsonResponse({'error': f'Erro ao deletar comentário: {str(e)}'}, status=500)
