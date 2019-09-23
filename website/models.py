from django.db import models
from django.contrib.auth.models import AbstractUser


class Profile(AbstractUser):
    birthday = models.DateField(null=True, blank=True)
    contact_number = models.CharField(max_length=20, blank=True, null=True)
    alter_ego = models.CharField(max_length=50, blank=True)
    image = models.ImageField(blank=True)

    def __str__(self):
        return f'{self.username}'


class Image(models.Model):
    image = models.ImageField(blank=True)
    user = models.ForeignKey(
        Profile,
        related_name='images',
        on_delete=models.CASCADE
    )


class Follow(models.Model):
    follower = models.ForeignKey(Profile, related_name='following', on_delete=models.CASCADE)
    followee = models.ForeignKey(Profile, related_name='followers', on_delete=models.CASCADE)
