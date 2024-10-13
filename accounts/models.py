from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    # add any custom fields here
    groups = models.ManyToManyField(
        'auth.Group',
        verbose_name='groups',
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        related_name='customuser_set',
        related_query_name='customuser',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name='user permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        related_name='customuser_set',
        related_query_name='customuser',
    )

    zip_code = models.CharField(max_length=9, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    state = models.CharField(max_length=2, blank=True, null=True)
    neighborhood = models.CharField(max_length=100, blank=True, null=True)
    gender = models.CharField(max_length=1, choices=[('M', 'Masculino'), ('F', 'Feminino')], blank=True, null=True)
    complement = models.CharField(max_length=100, blank=True, null=True)
    birth_date = models.DateField(null=True, blank=True)
    street = models.CharField(max_length=255, blank=True, null=True)
    number = models.CharField(max_length=10, blank=True, null=True)

    def __str__(self):
        return self.username
