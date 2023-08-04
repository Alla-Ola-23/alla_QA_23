import pytest
from modules.common.database import Database


@pytest.mark.copi
def test_database_connection():
    #завдання відправити тест запит і отримати відповідь, і прінт
    db = Database()
    db.test_connection()

@pytest.mark.copi
def test_check_all_users():
    #завдання дані про всіх користувачів і прінт
    db = Database()
    users = db.get_all_users()
    
    print(users)

@pytest.mark.copi
def test_check_user_sergii():
    #визначити адресу для доставки товару покупцю з ім'ям Сергій
    db = Database()
    user = db.get_user_address_by_name('Sergii')

    assert user[0][0] == 'Maydan Nezalezhnosti 1'
    assert user[0][1] == 'Kyiv'
    assert user[0][2] == '3127'
    assert user[0][3] == 'Ukraine'

@pytest.mark.copi
def test_product_qnt_update():
    db = Database()
    db.update_product_qnt_by_id(1, 25)
    water_qnt = db.select_product_qnt_by_id(1)

    assert water_qnt[0][0] == 25
