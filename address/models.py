from django.db import models
from django.contrib.auth.models import User

class Address(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    street = models.CharField(max_length=255)
    neighborhood = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    number = models.CharField(max_length=10, null=True, blank=True)
    complement = models.CharField(max_length=255, null=True, blank=True)
    state = models.CharField(max_length=2)
    zipcode = models.CharField(max_length=10)

    # ... outros campos e métodos, se necessário
