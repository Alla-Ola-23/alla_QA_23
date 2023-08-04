import sqlite3

class Database():
#мабуть для створення колекції запитів до бд
    def __init__(self) -> None:
        self.connection = sqlite3.connect(r'/Users/allakyrylova/alla_prog_/git_rep_QA23/alla_QA_23' + r'/become_qa_auto.db')
       #потрібна модулю sqlite3 для взаємодії з бд
        self.cursor = self.connection.cursor()
        #виконує наші команди в бд

    def test_connection(self):
        #метод обґкту 
        sqlite_select_Query = "SELECT sqlite_version();"
        self.cursor.execute(sqlite_select_Query)
        #виконання запиту в бд
        record = self.cursor.fetchall()
        #отримання результатів виконання запиту і запис їх у змінну
        print(f"Connected successfully. SQLite Database Version is: {record}")

    def get_all_users(self):
        query = "SELECT name, address, city FROM customers"
        #sql запит
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record
    
    def get_user_address_by_name(self, name):
        query = f"SELECT address, city, postalCode, country FROM customers WHERE name = '{name}'"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record
    
    def update_product_qnt_by_id(self, product_id, qnt):
        query = f"UPDATE products SET quantity = {qnt} WHERE id = {product_id}"
        self.cursor.execute(query)
        self.connection.commit()
        #підтвердження змін в базі даних, щоб випадково не змінити інші дані
        
    def select_product_qnt_by_id(self, product_id):
        #перевірка кількості в певному полі для певного продукту
        query = f"SELECT quantity FROM products WHERE id = {product_id}"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        #отримати результати і записати їх у змінну
        return record
    
    def insert_product(self, product_id, name, description, qnt):
        #вставлення даних в таблицю products
        query = f"INSERT OR REPLACE INTO products (id, name, description, quantity) \
            VALUES ({product_id}, '{name}', '{description}', {qnt})"
        self.cursor.execute(query)
        self.connection.commit()

    def delete_product_by_id(self, product_id):
        #видалення продукту за Ід
        query = f"DELETE FROM products WHERE id = {product_id}"
        self.cursor.execute(query)
        self.connection.commit()

    def get_detailed_orders(self):
        query = "SELECT orders.id, customers.name, products.name, \
            products.description, orders.order_date \
            FROM orders \
            JOIN customers ON orders.customer_id = customers.id \
            JOIN products ON orders.product_id = products.id"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record
    
    










