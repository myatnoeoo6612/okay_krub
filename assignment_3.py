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

    def start_engine(self):
        if self.make == "Unknown":
            raise ValueError("Cannot start the engine of an unknown make.")
        print("Engine started.")

car1 = Car("Toyota", "Corolla")
car1.print_car_info()
try:
    car1.start_engine()
except ValueError as e:
    print(f"Error: {e}")

car2 = Car("Unknown", "ModelX")
car2.print_car_info()
try:
    car2.start_engine()
except ValueError as e:
    print(f"Error: {e}")
