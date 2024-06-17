import sqlite3

class ProductDB:
    def _init_(self):
        self.connection = sqlite3.connect("online_store.db")
        self.cursor = self.connection.cursor()

    def add_product(self, name, price):
        self.cursor.execute("INSERT INTO products (name, price) VALUES (?, ?)", (name, price))
        self.connection.commit()

    def get_all_products(self):
        self.cursor.execute("SELECT * FROM products")
        return self.cursor.fetchall()

    def close(self):
        self.connection.close()