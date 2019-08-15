from django.contrib import admin

# Register your models here.
from .models import Image, Profile

admin.site.register(Image)
admin.site.register(Profile)
