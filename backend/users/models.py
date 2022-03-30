from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class UserData(models.Model):
    user = models.ForeignKey(User, related_name='infos', on_delete=models.CASCADE)
    favourite_genres = models.CharField(max_length=255)
    favourite_cinemas = models.CharField(max_length=255)

    class Meta:
        ordering = ('user',)

    def __str__(self):
        return self.user