import pytest

from website.models import Image
from django.contrib.auth.models import User


@pytest.fixture
def data():
    user = User.objects.create_user(username='test', password='test')
    image = Image.objects.create(image='test.jpg', user=user)
    return user, image
