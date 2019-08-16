import pytest

from website.models import Image
from django.contrib.auth.models import User


@pytest.fixture
def data():
    user = User.objects.create_user(username='john', password='john')
    image = Image.objects.create(image='john.jpg', user=user)
    return user, image
