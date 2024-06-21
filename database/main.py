from customers import CustomerDB
from products import ProductDB
from orders import OrderDB
from order_items import OrderItemDB

def main():
    customer_db = CustomerDB()
    product_db = ProductDB()
    order_db = OrderDB()
    order_item_db = OrderItemDB()

    while True:
        print("\n1. Add new customer")
        print("2. Add new product")
        print("3. Create new order")
        print("4. Add item to order")
        print("5. Get all customers")
        print("6. Get all products")
        print("7. Get all orders")
        print("8. Get all order items")
        print("9. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter customer's name: ")
            email = input("Enter customer's email: ")
            customer_db.add_customer(name, email)
        elif choice == "2":
            name = input("Enter product's name: ")
            price = float(input("Enter product's price: "))
            product_db.add_product(name, price)
        elif choice == "3":
            customer_id = int(input("Enter customer ID: "))
            order_date = input("Enter order date (YYYY-MM-DD): ")
            order_id = order_db.add_order(customer_id, order_date)
            print(f"Order {order_id} created.")
        elif choice == "4":
            order_id = int(input("Enter order ID: "))
            product_id = int(input("Enter product ID: "))
            quantity = int(input("Enter quantity: "))
            order_item_db.add_order_item(order_id, product_id, quantity)
        elif choice == "5":
            customers = customer_db.get_all_customers()
            for customer in customers:
                print(f"Customer ID: {customer[0]}, Name: {customer[1]}, Email: {customer[2]}")
        elif choice == "6":
            products = product_db.get_all_products()
            for product in products:
                print(f"Product ID: {product[0]}, Name: {product[1]}, Price: {product[2]}")
        elif choice == "7":
            orders = order_db.get_all_orders()
            for order in orders:
                print(f"Order ID: {order[0]}, Customer Name: {order[1]}, Customer Email: {order[2]}, Order Date: {order[3]}")
        elif choice == "8":
            order_items = order_item_db.get_all_order_items()
            for item in order_items:
                print(f"Order Item ID: {item[0]}, Order ID: {item[1]}, Product Name: {item[2]}, Product Price: {item[3]}, Quantity: {item[4]}")
        elif choice == "9":
            customer_db.close()
            product_db.close()
            order_db.close()
            order_item_db.close()
            break
        else:
            print("Invalid choice. Try again.")

if __name__== "__main__":
    main()
