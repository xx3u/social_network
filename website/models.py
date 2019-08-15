from django.db import models
from django.contrib.auth.models import User


class Image(models.Model):
    image = models.ImageField(blank=True)
    user = models.ForeignKey(
        User, related_name='images',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.user


class Profile(models.Model):
    # user = models.OneToOneField(User, on_delete=models.CASCADE)
    # birthday = models.DateTimeField()
    # contact_number = models.IntegerField()
    
