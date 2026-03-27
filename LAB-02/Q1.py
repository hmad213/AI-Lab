class Vehicle:
    def __init__(self, b):
        self.brand = b

class Car(Vehicle):
    def __init__(self, b, m):
        super().__init__(b)
        self.model = m

class ElectricCar(Car):
    def __init__(self, b, m, bc):
        super().__init__(b, m)
        self.battery_capacity = bc

a = ElectricCar("Tesla", 2024, 5000)
print("Brand:", a.brand)
print("Model:", a.model)
print("Battery Capacity:", a.battery_capacity)