from django.db import models
from django.contrib.auth.models import User, AbstractUser
from django.conf import settings


class Image(models.Model):
    image = models.ImageField(blank=True)
    user = models.ForeignKey(
        User,
        related_name='images',
        on_delete=models.CASCADE
    )


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    birthday = models.DateField(null=True, blank=True)
    contact_number = models.CharField(max_length=20, null=True)
