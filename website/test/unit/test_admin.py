from website.models import Profile, Story


def test_profile_str(db, data):
    profile = Profile.objects.get(username='idea')
    assert str(profile) == 'idea'


def test_story_str(db, data):
    story = Story.objects.get(title='storytale')
    assert str(story) == 'storytale'
