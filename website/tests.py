def test_model(db, data):
    user, image = data
    assert image.user.username == 'john'
    assert image.image == 'john.jpg'


def test_admin_str(db, data):
    user, image = data
    assert str(image) == 'john'
