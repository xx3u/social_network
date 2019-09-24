import pytest

from website.models import Image, CustomUser


@pytest.fixture
def data():
    user = CustomUser.objects.create_user(username='test', password='test')
    image = Image.objects.create(image='test.jpg', user=user)
    return user, image
