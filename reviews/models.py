from django.db import models

class Review(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey('auth.User', on_delete=models.PROTECT)
    workshop = models.ForeignKey('workshops.Workshop', on_delete=models.PROTECT)
    rating = models.IntegerField()
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)