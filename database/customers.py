
# import sqlite3

# class CustomerDB:
#     #access database
#     def _init_(self):
#         self.connection = sqlite3.connect("online_store.db")
#         self.cursor = self.connection.cursor()
# #add sth
#     def add_customer(self, name, email):
#         self.cursor.execute("INSERT INTO customers (name, email) VALUES (?, ?)", (name, email))
#         self.connection.commit()
# #returns all customers
#     def get_all_customers(self):
#         self.cursor.execute("SELECT * FROM customers")
#         return self.cursor.fetchall()
# #close db
#     def close(self):
#         self.connection.close()