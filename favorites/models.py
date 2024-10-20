from django.conf import settings
from django.db import models
from django.contrib.auth import get_user_model

class Favorite(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    workshop = models.ForeignKey('workshops.Workshop', on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @classmethod
    def delete_favorite(cls, user_id, favorite_id):
        try:
            favorite = cls.objects.get(id=favorite_id, user_id=user_id)
            favorite.delete()
            return True, "Favorito deletado com sucesso."
        except cls.DoesNotExist:
            return False, "Favorito não encontrado ou não pertence ao usuário."
        except Exception as e:
            return False, f"Erro ao deletar favorito: {str(e)}"
