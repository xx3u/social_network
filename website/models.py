from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    birthday = models.DateField(null=True, blank=True)
    contact_number = models.CharField(max_length=20, blank=True)


class Image(models.Model):
    image = models.ImageField(blank=True)
    user = models.ForeignKey(
        CustomUser,
        related_name='images',
        on_delete=models.CASCADE
    )
