class Car:
    def __init__(self, make=None, model=None):
        self.make = make
        self.model = model

    def print_car_info(self):
        try:
            if self.make is None or self.model is None:
                raise AttributeError("Make or model is not set.")
            print(f"Make: {self.make}, Model: {self.model}")
        except AttributeError as e:
            print(f"Error: {e}")

car1 = Car("Toyota", "Corolla")
car1.print_car_info()

car2 = Car()
car2.print_car_info()
