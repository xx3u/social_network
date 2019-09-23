import pytest

from website.models import Image, Profile


@pytest.fixture
def data():
    user = Profile.objects.create_user(username='test', password='test')
    image = Image.objects.create(image='test.jpg', user=user)
    return user, image
