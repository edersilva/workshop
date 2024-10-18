from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Favorite

@login_required
def list_favorites(request):
    favorites = Favorite.objects.filter(user=request.user)
    context = {
        'favorites': favorites,
        'title': 'Favoritos',
    }
    return render(request, 'favorites/list.html', context)

