cart = {}


def add_product():
    name = input("Enter product name: ").strip()

    if name in cart:
        print("Product already exists in cart!")
        return

    try:
        price = float(input("Enter product price: "))
        quantity = int(input("Enter quantity: "))

        if price < 0 or quantity <= 0:
            print("Price must be non-negative and quantity must be greater than 0.")
            return

        cart[name] = {
            "price": price,
            "quantity": quantity
        }

        print(f"{name} added to cart successfully!")

    except ValueError:
        print("Please enter valid price and quantity.")


def remove_product():
    name = input("Enter product name to remove: ").strip()

    if name in cart:
        del cart[name]
        print(f"{name} removed from cart.")
    else:
        print("Product not found in cart.")


def update_quantity():
    name = input("Enter product name: ").strip()

    if name not in cart:
        print("Product not found in cart.")
        return

    try:
        quantity = int(input("Enter new quantity: "))

        if quantity < 0:
            print("Quantity cannot be negative.")
        elif quantity == 0:
            del cart[name]
            print(f"{name} removed from cart.")
        else:
            cart[name]["quantity"] = quantity
            print(f"Quantity of {name} updated successfully.")

    except ValueError:
        print("Please enter a valid quantity.")


def view_cart():
    if not cart:
        print("\nYour cart is empty.")
        return

    print("\n========== YOUR CART ==========")
    print(f"{'Product':<15}{'Price':<12}{'Qty':<8}{'Total':<12}")
    print("-" * 47)

    for name, details in cart.items():
        price = details["price"]
        quantity = details["quantity"]
        total = price * quantity

        print(f"{name:<15}₹{price:<11.2f}{quantity:<8}₹{total:.2f}")


def calculate_total():
    if not cart:
        print("\nYour cart is empty.")
        return

    total_bill = 0

    for details in cart.values():
        total_bill += details["price"] * details["quantity"]

    print(f"\nTotal Bill: ₹{total_bill:.2f}")


while True:
    print("\n========== SHOPPING CART ==========")
    print("1. Add Product")
    print("2. Remove Product")
    print("3. Update Quantity")
    print("4. View Cart")
    print("5. Calculate Total")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_product()

    elif choice == "2":
        remove_product()

    elif choice == "3":
        update_quantity()

    elif choice == "4":
        view_cart()

    elif choice == "5":
        calculate_total()

    elif choice == "6":
        print("Thank you for using the Shopping Cart!")
        break

    else:
        print("Invalid choice. Please try again.")