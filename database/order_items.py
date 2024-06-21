import sqlite3
#access items in db
class OrderItemDB:
    def _init_(self):
        self.connection = sqlite3.connect("online_store.db")
        self.cursor = self.connection.cursor()
#add to db
    def add_order_item(self, order_id, product_id, quantity):
        #allows you to insert data in table
        self.cursor.execute("INSERT INTO order_items (order_id, product_id, quantity) VALUES (?, ?, ?)", (order_id, product_id, quantity))
        self.connection.commit()
#get items
    def get_all_order_items(self):
        self.cursor.execute('''
            SELECT order_items.id, orders.id AS order_id, products.name, products.price, order_items.quantity
            FROM order_items
            JOIN orders ON order_items.order_id = orders.id
            JOIN products ON order_items.product_id = products.id
        ''')
        return self.cursor.fetchall()

    def close(self):
        self.connection.close()
