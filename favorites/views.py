from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from .models import Favorite
import logging

logger = logging.getLogger(__name__)

@login_required
def list_favorites(request):
    favorites = Favorite.objects.filter(user=request.user)
    context = {
        'favorites': favorites,
        'title': 'Favoritos',
    }
    return render(request, 'favorites/list.html', context)

@login_required
@require_http_methods(["DELETE"])
def delete_favorite(request, favorite_id):
    try:
        favorite = Favorite.objects.get(id=favorite_id, user=request.user)
        favorite.delete()
        logger.info(f"Favorito {favorite_id} deletado com sucesso.")
        return JsonResponse({'message': 'Favorito deletado com sucesso.'}, status=200)
    except Favorite.DoesNotExist:
        logger.warning(f"Tentativa de deletar favorito inexistente ou não pertencente ao usuário. ID: {favorite_id}, Usuário: {request.user.id}")
        return JsonResponse({'error': 'Favorito não encontrado ou não pertence ao usuário atual.'}, status=404)
    except Exception as e:
        logger.error(f"Erro ao deletar favorito {favorite_id}: {str(e)}")
        return JsonResponse({'error': f'Erro ao deletar favorito: {str(e)}'}, status=500)
