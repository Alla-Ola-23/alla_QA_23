import pytest
from modules.common.database import Database


@pytest.mark.database
def test_database_connection(data_base):
    #завдання відправити тест запит і отримати відповідь, і прінт
    data_base.test_connection()

@pytest.mark.database
def test_check_all_users(data_base):
    #завдання дані про всіх користувачів і прінт
    users = data_base.get_all_users()
    print(users)

@pytest.mark.database
def test_check_user_sergii(data_base):
    #визначити адресу для доставки товару покупцю з ім'ям Сергій
    user = data_base.get_user_address_by_name('Sergii')
    assert user[0][0] == 'Maydan Nezalezhnosti 1'
    assert user[0][1] == 'Kyiv'
    assert user[0][2] == '3127'
    assert user[0][3] == 'Ukraine'

@pytest.mark.database
def test_product_qnt_update(data_base):
    data_base.update_product_qnt_by_id(1, 25)
    water_qnt = data_base.select_product_qnt_by_id(1)

    assert water_qnt[0][0] == 25

@pytest.mark.database
def test_product_insert(data_base):
    data_base.insert_product(4, 'печиво', 'солодке', 30)
    water_qnt = data_base.select_product_qnt_by_id(4)
    assert water_qnt[0][0] == 30
    
@pytest.mark.database
def test_product_delete(data_base):
    #перевірка можливості видалення з бд. 
    data_base.insert_product(99, 'тестові', 'дані', 999)
    #хитрість : спочатку створюємо дані, потім видаляємо
    data_base.delete_product_by_id(99)
    qnt = data_base.select_product_qnt_by_id(99)
    #дані кількості видаленого товару 
    assert len(qnt) == 0

@pytest.mark.database
def test_detailed_orders(data_base):
    orders = data_base.get_detailed_orders()
    print("Замовлення", orders)
    #Check quantity of orders equal to 1
    assert len(orders) == 1

    #Check structure of data
    assert orders[0][0] == 1
    assert orders[0][1] == 'Sergii'
    assert orders[0][2] == 'солодка вода'
    assert orders[0][3] == 'з цукром'

