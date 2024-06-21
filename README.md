# Phase 3 project

# Description
This project is a command-line interface application designed for managing an online store.It allows users to interact with the database to add customers, products, orders, and order items, as well as retrieve information about them. The application is built using Python and SQLite for database management.

## CLI Script
main.py
The main.py script serves as the entry point for the CLI application. It provides a menu-driven interface where users can perform various actions such as adding customers and products, creating orders, adding items to orders, and retrieving information about customers, products, orders, and order items.

## Functions
`main()`: This function initializes instances of database classes (CustomerDB, ProductDB, OrderDB, OrderItemDB) and presents a menu to the user. Depending on the user's choice, it calls corresponding methods from these database classes to perform CRUD operations on the database.

## Functionality Overview:

`Add new customer`: Prompts the user to enter customer details (name and email) and adds them to the database using CustomerDB.add_customer().
`Add new product`: Prompts the user to enter product details (name and price) and adds them to the database using ProductDB.add_product().
`Create new order`: Prompts the user to enter customer ID and order date, then creates a new order in the database using OrderDB.add_order().
`Add item to order`: Prompts the user to enter order ID, product ID, and quantity, then adds an item to an existing order using OrderItemDB.add_order_item().
`Get all customers`: Retrieves and displays all customers from the database using CustomerDB.get_all_customers().
`Get all products`: Retrieves and displays all products from the database using ProductDB.get_all_products().
`Get all orders`: Retrieves and displays all orders from the database using OrderDB.get_all_orders().
`Get all order items`: Retrieves and displays all order items from the database using OrderItemDB.get_all_order_items().
`Error Handling`: Error handling is implemented to catch exceptions that may occur during database operations, ensuring robustness and preventing crashes.

## Database Classes
`customers.py`
## Description
The customers.py file contains the CustomerDB class, responsible for managing operations related to customers in the database.

Functions
`add_customer(name, email)`: Inserts a new customer into the customers table with the provided name and email.
`get_all_customers()`: Retrieves all customers from the customers table and returns them as a list of tuples.

`products.py`
## Description
The products.py file contains the ProductDB class, which handles operations related to products in the database.

Functions
`add_product(name, price)`: Inserts a new product into the products table with the provided name and price.
`get_all_products()`: Retrieves all products from the products table and returns them as a list of tuples.


`orders.py`
## Description
The orders.py file houses the OrderDB class, responsible for managing operations related to orders in the database.

Functions
`add_order(customer_id, order_date)`: Creates a new order in the orders table with the provided customer ID and order date.
`get_all_orders()`: Retrieves all orders from the orders table, including associated customer details, and returns them as a list of tuples.


`order_items.py`
## Description
The order_items.py file contains the OrderItemDB class, handling operations related to order items in the database.

 Functions
`add_order_item(order_id, product_id, quantity)`: Inserts a new order item into the order_items table with the provided order ID, product ID, and quantity.
`get_all_order_items()`: Retrieves all order items from the order_items table, including associated order and product details, and returns them as a list of tuples.


## Project Structure
main.py: Entry point for the CLI application.
customers.py: Database class for managing customers.
products.py: Database class for managing products.
orders.py: Database class for managing orders.
order_items.py: Database class for managing order items.
online_store.db: SQLite database file storing customer, product, order, and order item data.


