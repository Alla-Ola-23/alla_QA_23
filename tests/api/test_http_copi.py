import pytest
import requests

@pytest.mark.copi
#http запит за допомогою методу get і вивід на екран
def test_first_request():
    r = requests.get('https://api.github.com/zen')
    print(r.text)


@pytest.mark.copi
def test_first_request():
    r = requests.get('https://api.github.com/zen')
    print(f"Response is {r.text}")

@pytest.mark.copi
#pytest -m http -s   команда виконання
#вивід текстового представлення response
def test_second_request():
    r = requests.get('https://api.github.com/users/defunkt')
    print(f"Response is {r.text}")


@pytest.mark.copi
#вивід головніх структур response, методу json(), і полей status_code і headers
def test_second_request():
    r = requests.get('https://api.github.com/users/defunkt')
    print(f"Response Body is {r.json()}")
    print(f"Response Status code is {r.status_code}")
    print(f"Response Headers are {r.headers}")

@pytest.mark.copi
#початок тестування response
#перевірка status_code на відповідність , 200
def test_second_request():
    r = requests.get('https://api.github.com/users/defunkt')
    print(f"Response Body is {r.json()}")
    assert r.status_code == 200
    print(f"Response Status code is {r.status_code}")
    print(f"Response Headers are {r.headers}")

@pytest.mark.copi
#метод json() до змінної, перевірка відповідності
def test_second_request():
    r = requests.get('https://api.github.com/users/defunkt')
    body = r.json()

    assert body['type'] == 'User'
    assert body['name'] == 'Chris Wanstrath'
    assert body['location'] == None
    assert r.status_code == 200
    print(f"Response Status code is {r.status_code}")
    print(f"Response Headers are {r.headers}")

@pytest.mark.copi
#перевірка заголовка сервера
def test_second_request():
    r = requests.get('https://api.github.com/users/defunkt')
    body = r.json()
    headers = r.headers

    assert body['type'] == 'User'
    assert body['name'] == 'Chris Wanstrath'
    assert body['location'] == None
    assert r.status_code == 200
    assert headers['Server'] == 'GitHub.com'

@pytest.mark.copi
#є адреса, яка працює не так, як очікується
#додаємо тест який намагається отримати і про корістувача сергія бутенко
#ми впевнені що такій користувач існує, але буде помилка,т.Як такого користувача не існує
#при статус код 200 помилка, при статус код 404 успіх 
def test_status_code_request():
    r = requests.get('https://api.github.com/users/sergii_butenko')

    assert r.status_code == 200

