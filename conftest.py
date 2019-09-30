import pytest

from website.models import Profile, Story


@pytest.fixture
def data():
    user = Profile.objects.create_user(
        username='idea',
        password='test',
        email='test@test.com',
        first_appearance='2019-09-11',
        alter_ego='admin',
        image='test.jpg',
        species='thought',
        place_of_origin='brain',
        team_affiliations='flash',
        abilities='existence'
    )
    story = Story.objects.create(
        title='storytale',
        author=user,
        text='once upon a time',
        pub_date='2019-09-11'
    )
    return user, story
