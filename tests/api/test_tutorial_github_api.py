#in file github.py
#class GitHub:

    #def get_user_defunkt(self):
        #користувач існує
     #   r = requests.get('https://api.github.com/users/defunkt')
      #  body = r.json()

       # return body
    
    #def get_non_exist_user(self):
        #користувача не існує
     #   r = requests.get('https://api.github.com/users/butenkosergii')
      #  body = r.json()

       # return body

#@pytest.mark.copi
#в цьому тесті використовуємо клієнта, який вікористовує GITHUB для комунікації 
#з сервером_ рядок 2
#завдання тесту відправити запит, що отримає дані, на сервер GITHUB
#отримавши відповідь, перевірити, що поле Логин співпадає з тим користувачем, якого ми шукали
#def test_user_exists():
 #   api = GitHub()
    #ініціація екземпляра класу
  #  user = api.get_user_defunkt()
    #отримання користувача

   # assert user['login'] == 'defunkt'


#@pytest.mark.copi
#завдання тесту сервер буде працювати нормально, якщо ми запитаємо у нього і про
#неіснуючого користувача, перевірити, що поле Логин співпадає з тим користувачем, якого ми шукали
#def test_user_not_exists():
 #   api = GitHub()
    #ініціація екземпляра класу
  #  r = api.get_non_exist_user()
    #отримання користувача
   # print(r)
    #спочатку прінт, щобб вибраті дани для тестування
    #assert r['message'] == 'Not Found'
    #потім ассерт