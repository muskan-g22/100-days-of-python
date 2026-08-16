# 87	Create a Vehicle hierarchy using inheritance.
# Parent class
class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display_info(self):
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")

    def start(self):
        print("Vehicle is starting...")


# Child class
class Car(Vehicle):
    def __init__(self, brand, model, doors):
        super().__init__(brand, model)
        self.doors = doors

    def start(self):
        print("Car starts with a key/button.")

    def display_info(self):
        super().display_info()
        print(f"Doors: {self.doors}")


# Child class
class Bike(Vehicle):
    def __init__(self, brand, model, engine_cc):
        super().__init__(brand, model)
        self.engine_cc = engine_cc

    def start(self):
        print("Bike starts with a self-start.")

    def display_info(self):
        super().display_info()
        print(f"Engine: {self.engine_cc} CC")


# Creating objects
car = Car("Toyota", "Fortuner", 4)
bike = Bike("Royal Enfield", "Classic 350", 350)

print("Car Details:")
car.display_info()
car.start()

print("\nBike Details:")
bike.display_info()
bike.start()