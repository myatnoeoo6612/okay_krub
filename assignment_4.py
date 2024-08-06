class Car:
    def __init__(self, make=None, model=None, year=None, fuel_level=0):
        self.make = make
        self.model = model
        self.year = year
        self.fuel_level = fuel_level

    def print_car_info(self):
        try:
            if self.make is None or self.model is None or self.year is None:
                raise AttributeError("Make, model, or year is not set.")
            print(f"Make: {self.make}, Model: {self.model}, Year: {self.year}")
        except AttributeError as e:
            print(f"Error: {e}")

    def start_engine(self):
        if self.make == "Unknown":
            raise ValueError("Cannot start the engine of an unknown make.")
        print("Engine started.")

    def check_fuel(self):
        if self.fuel_level < 5:
            raise ValueError("Fuel level is too low!")

    def drive(self, distance):
        self.fuel_level -= distance
        self.check_fuel()
        print(f"Drove {distance} miles. Fuel level: {self.fuel_level}")

my_car = Car("Toyota", "Corolla", 2022, 10)

try:
    my_car.drive(3)  
    my_car.drive(4)  
    my_car.drive(3)  
except ValueError as e:
    print(e)
