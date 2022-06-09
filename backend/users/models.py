from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from cinema.models import Genre, Building

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    favourite_genres = models.ManyToManyField(Genre, blank=True)
    favourite_cinemas = models.ManyToManyField(Building, blank=True)

    class Meta:
        ordering = ('user',)

    def __str__(self):
        return f'{self.user}'

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()