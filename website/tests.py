def test_model(db, data):
    user, image = data
    assert image.user.username == 'john'
    assert image.image == 'john.jpg'
