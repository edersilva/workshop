from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.conf import settings

class CustomUser(AbstractUser):
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

class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    birth_date = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=10, choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], blank=True)
    street = models.CharField(max_length=255, blank=True)
    number = models.CharField(max_length=10, blank=True)
    complement = models.CharField(max_length=255, blank=True)
    neighborhood = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=255, blank=True)
    state = models.CharField(max_length=2, blank=True)  # Assuming state abbreviations
    zip_code = models.CharField(max_length=10, blank=True)
    groups = models.ManyToManyField(
        Group,
        verbose_name=('groups'),
        blank=True,
        help_text=(
            'The groups this user belongs to. A user will get all permissions '
            'granted to each of their groups.'
        ),
        related_name="userprofile_set",
        related_query_name="userprofile",
    )
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name=('user permissions'),
        blank=True,
        help_text=('Specific permissions for this user.'),
        related_name="userprofile_set",
        related_query_name="userprofile",
    )

    def __str__(self):
        return self.user.username
