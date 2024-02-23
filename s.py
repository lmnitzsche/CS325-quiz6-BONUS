# s.py - Single Responsibility Principle (SRP) Example
# A class should have one and only one reason to change, meaning that a class should have only one job.

class Customer:
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone

class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class ShippingAddress:
    def __init__(self, address):
        self.address = address

class OrderDetails:
    def __init__(self, customer, items, shipping_address):
        self.customer = customer
        self.items = items
        self.shipping_address = shipping_address

class OrderCalculator:
    @staticmethod
    def calculate_total_order_cost(order_details):
        total_cost = 0
        for item in order_details.items:
            total_cost += item.price
        return total_cost

class OrderValidator:
    @staticmethod
    def validate_order_data(order_details):
        if not order_details.items:
            print("Error: No items in the order")
            return False
        if not order_details.shipping_address:
            print("Error: Shipping address is missing")
            return False
        return True

class EmailSender:
    @staticmethod
    def send_order_confirmation_email(customer):
        print(f"Order confirmation email sent to {customer.email}")

class InventoryUpdater:
    @staticmethod
    def update_inventory_levels():
        print("Inventory levels updated after order processing")

def main():
    # Dummy data
    customer = Customer(name="Logan Nitzsche", email="lnitzsc@siue.edu", phone="123-456-7890")
    items = [Item(name="Xbox", price=10), Item(name="PlayStation", price=20)]
    shipping_address = ShippingAddress(address="123 Main St, Edwardsville, Illinois")
    order_details = OrderDetails(customer=customer, items=items, shipping_address=shipping_address)
    
    # Calculate and output total cost
    total_cost = OrderCalculator.calculate_total_order_cost(order_details)
    print("Total order cost:", total_cost)

    # Validate order data
    is_valid = OrderValidator.validate_order_data(order_details)
    if is_valid:
        print("Order data is valid")
    else:
        print("Order data is not valid")

    # Send order confirmation email
    EmailSender.send_order_confirmation_email(customer)

    # Update inventory levels
    InventoryUpdater.update_inventory_levels()

if __name__ == "__main__":
    main()
