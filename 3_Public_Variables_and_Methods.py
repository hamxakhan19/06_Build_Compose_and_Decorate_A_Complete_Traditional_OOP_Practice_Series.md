class Car:
    def __init__(self, brand):
        self.brand = brand

    def start(self):
        print(f"{self.brand} car is starting.")

# Example
car = Car("Toyota")
print(car.brand)
car.start()
