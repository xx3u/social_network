from django.db import models
from django.contrib.auth.models import AbstractUser


class Profile(AbstractUser):
    first_appearance = models.DateField(null=True, blank=True)
    alter_ego = models.CharField(max_length=50, blank=True)
    image = models.ImageField(blank=True)
    species = models.CharField(max_length=50, blank=True)
    place_of_origin = models.CharField(max_length=50, blank=True)
    team_affiliations = models.TextField(blank=True)
    abilities = models.TextField(blank=True)

    def __str__(self):
        return f'{self.username}'


class Story(models.Model):
    title = models.CharField(max_length=50)
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    text = models.TextField(blank=True)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.title


class Follow(models.Model):
    follower = models.ForeignKey(Profile, related_name='following', on_delete=models.CASCADE)
    followee = models.ForeignKey(Profile, related_name='followers', on_delete=models.CASCADE)
