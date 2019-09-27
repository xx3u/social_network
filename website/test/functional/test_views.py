from lxml import html
from django.urls import reverse


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
    print(a[0].text)
    assert len(a) == 1
    assert a[0].text == 'Hi, idea!\n            '


def test_register_view(db, client, data):
    response = client.get('/register/')
    assert response.status_code == 200

    response = client.post(
        '/register/', {'username': 'idea', 'password': 'test'},
    )
    assert response.status_code == 200


def test_about(db, client, data):
    response = client.get('/about/')
    assert response.status_code == 200


def test_profile(db, client, data):
    client.login(username='idea', password='test')
    response = client.get('/profile/', follow=True)
    assert response.status_code == 200

    response = response.content.decode('utf-8')
    response = html.fromstring(response)
    selector = 'body > div > div > div > div > h2'
    profile = response.cssselect(selector)
    assert profile[0].text == 'idea'

    selector = 'body > div > div > div > div > p:nth-child(4)'
    species = response.cssselect(selector)
    assert species[0].text == 'Species: thought'
