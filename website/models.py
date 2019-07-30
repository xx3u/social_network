from django.db import models


# Create your models here.
class Profile(models.Model):
    username = models.CharField(max_length=50)
    # full_name = models.CharField(max_length=50)
    # email = models.CharField(max_length=50)
    # password = models.CharField(max_length=50)
    # birthday = models.DateTimeField()
    # contact_number = models.IntegerField()
    image = models.ImageField(blank=True)

    def __str__(self):
        return self.username
