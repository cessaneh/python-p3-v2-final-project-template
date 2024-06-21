import sqlite3

class OrderDB:
    def _init_(self):
        self.connection = sqlite3.connect("online_store.db")
        self.cursor = self.connection.cursor()

    def add_order(self, customer_id, order_date):
        self.cursor.execute("INSERT INTO orders (customer_id, order_date) VALUES (?, ?)", (customer_id, order_date))
        self.connection.commit()
        return self.cursor.lastrowid

    def get_all_orders(self):
        self.cursor.execute('''
            SELECT orders.id, customers.name, customers.email, orders.order_date
            FROM orders
            JOIN customers ON orders.customer_id = customers.id
        ''')
        return self.cursor.fetchall()

    def close(self):
        self.connection.close()
