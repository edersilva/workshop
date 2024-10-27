from .models import Favorite

def is_workshop_favorited(user, workshop):
    if user.is_authenticated:
        return Favorite.objects.filter(user=user, workshop=workshop).exists()
    return False

