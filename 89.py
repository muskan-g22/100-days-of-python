# 89	Create a shopping cart using OOP.
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def display(self):
        print(f"{self.name} - ₹{self.price}")


class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, product):
        self.items.append(product)
        print(f"{product.name} added to cart.")

    def remove_item(self, product_name):
        for product in self.items:
            if product.name.lower() == product_name.lower():
                self.items.remove(product)
                print(f"{product.name} removed from cart.")
                return

        print("Product not found in cart.")

    def display_cart(self):
        if not self.items:
            print("Cart is empty.")
            return

        print("\n--- Shopping Cart ---")
        for product in self.items:
            product.display()

    def total_price(self):
        total = sum(product.price for product in self.items)
        print(f"Total Price: ₹{total}")


# Creating products
laptop = Product("Laptop", 55000)
mouse = Product("Mouse", 800)
keyboard = Product("Keyboard", 1500)

# Creating shopping cart
cart = ShoppingCart()

# Add products
cart.add_item(laptop)
cart.add_item(mouse)
cart.add_item(keyboard)

# Display cart
cart.display_cart()

# Calculate total
cart.total_price()

# Remove product
cart.remove_item("Mouse")

# Display updated cart
cart.display_cart()
cart.total_price()