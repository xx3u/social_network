from lxml import html
from django.urls import reverse
from website.forms import UserRegisterForm


def test_login(db, client, data):
    login = client.login(username='idea', password='test')
    response = client.post(
        '/login/', {'username': 'idea', 'password': 'test'}, follow=True
    )
    assert login is True
    assert response.status_code == 200


def test_login_fail(db, client, data):
    response = client.post(
        '/login/', {'username': 'idea', 'password': 'wrongpassword'}
    )
    assert response.status_code == 200
    assert 'Please enter a correct username and password.' in response.content.decode()


def test_logout(db, client, data):
    client.login(username='idea', password='test')
    response = client.post('/logout/', follow=True)
    assert response.status_code == 200
    response = response.content.decode('utf-8')
    response = html.fromstring(response)
    assert len(response.cssselect('input[name="username"]')) == 1


def test_home(db, client, data):
    client.login(username='idea', password='test')
    response = client.get('/')
    assert response.status_code == 200
    response = response.content.decode('utf-8')
    response = html.fromstring(response)

    # Assert there is a link to home page
    url = reverse('home')
    selector = 'a.nav-link[href="{}"]'.format(url)
    a = response.cssselect(selector)
    assert len(a) == 1
    assert a[0].text == 'Home'

    # Assert there is username in navbar
    selector = 'a.nav-link[id="username"]'
    a = response.cssselect(selector)
    assert len(a) == 1
    assert a[0].text == 'Hi, idea!\n            '


def test_register_view(db, client, data):
    response = client.get('/register/')
    assert response.status_code == 200

    response = client.post(
        '/register/', {'username': 'idea', 'password': 'test'}
    )
    assert response.status_code == 200

    # Assert that new user fills all required fields for registration and register form is valid
    valid_data = {
        'username': 'xx3u', 'email': 'xx3u@example.com', 'password1': 'qwerty1234!', 'password2': 'qwerty1234!'
        }
    form = UserRegisterForm(valid_data)
    assert form.is_valid() is True

    # Assert that new user fills invalid password for required fields during registration
    wrong_password = {
        'username': 'xx3u', 'email': 'xx3u@example.com', 'password1': '11223344', 'password2': '11223344'
        }
    form = UserRegisterForm(wrong_password)
    assert form.is_valid() is False
    assert form['password2'].errors == ['This password is too common.', 'This password is entirely numeric.']

    # Assert that new user does not fill required password fields during registration
    wrong_data = {
        'username': 'xx3u', 'email': 'xx3u@example.com'
        }
    form = UserRegisterForm(wrong_data)
    assert form.is_valid() is False
    assert form['password1'].errors == ['This field is required.']

    # Assert that after successfull registration,
    # user gets message 'Your account has been created! You are now able to log in'
    response = client.post(
        '/register/',
        {
            'username': 'xx3u',
            'email': 'xx3u@example.com',
            'password1': 'qwerty1234!',
            'password2': 'qwerty1234!'
        }, follow=True
    )
    messages = list(response.context['messages'])
    assert len(messages) == 1
    assert str(messages[0]) == 'Your account has been created! You are now able to log in'

    assert response.status_code == 200


def test_about(db, client, data):
    response = client.get('/about/')
    assert response.status_code == 200

    # Assert text 'About Page' on about url
    response = response.content.decode('utf-8')
    response = html.fromstring(response)
    selector = 'h1'
    profile = response.cssselect(selector)
    assert profile[0].text == 'About Page'


def test_profile(db, client, data):
    client.login(username='idea', password='test')
    response = client.get('/profile/', follow=True)
    assert response.status_code == 200

    # Assert that profile url includes username in <h2>
    response = response.content.decode('utf-8')
    response = html.fromstring(response)
    selector = 'body > div > div > div > div > h2'
    profile = response.cssselect(selector)
    assert profile[0].text == 'idea'

    # Assert that profile page details are correct
    selector = 'body > div > div > div > div > p:nth-child(4)'
    species = response.cssselect(selector)
    assert species[0].text == 'Species: thought'
    selector = 'body > div > div > div > div > p:nth-child(5)'
    species = response.cssselect(selector)
    assert species[0].text == 'Place of origin: brain'
    selector = 'body > div > div > div > div > p:nth-child(7)'
    species = response.cssselect(selector)
    assert species[0].text == 'Abilities: existence'
