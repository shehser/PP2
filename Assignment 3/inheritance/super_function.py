class Vehicle:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed

    def display_info(self):
        print(f"Brand: {self.brand}, Speed: {self.speed} km/h")

class Car(Vehicle):
    def __init__(self, brand, speed, fuel_type):
        # super() initializes the attributes from the parent constructor without repetition
        super().__init__(brand, speed)
        self.fuel_type = fuel_type  # Attribute specific only to Car instances

    def display_car_info(self):
        super().display_info()  # Invoking parent method through super()
        print(f"Fuel Type: {self.fuel_type}")

my_car = Car("Toyota", 180, "Petrol")
my_car.display_car_info()
