from lxml import html
from django.contrib.auth.models import User
from django.urls import reverse

from website.models import Image, Profile

def test_login(db, client, data):
    response = client.post(
        '/login/', {'username': 'test', 'password': 'test'}
    )
    assert response.status_code == 302


def test_login_fail(db, client, data):
    response = client.post(
        '/login/', {'username': 'test', 'password': 'wrongpassword'}
    )
    assert response.status_code == 200
    assert b'Please enter a correct username and password.' in response.content


def test_logout(db, client, data):
    client.login(username='test', password='test')
    response = client.post('/logout/', follow=True)
    assert response.status_code == 200
    response = response.content.decode('utf-8')
    response = html.fromstring(response)
    assert len(response.cssselect('input[name="username"]')) == 1


def test_home(db, client, data):
    client.login(username='test', password='test')
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
    assert a[0].text == 'Hi, test!\n            '
