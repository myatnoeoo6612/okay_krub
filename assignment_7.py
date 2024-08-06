class OverSpeedError(Exception):
    def __init__(self, message="Speed limit exceeded!"):
        self.message = message
        super().__init__(self.message)

class Car:
    def __init__(self, make=None, model=None, year=None, fuel_level=0, speed=0):
        self.make = make
        self.model = model
        self.year = year
        self.fuel_level = fuel_level
        self.speed = speed
        self.color = None

    def print_car_info(self):
        try:
            if self.make is None or self.model is None or self.year is None:
                raise AttributeError("Make, model, or year is not set.")
            print(f"Make: {self.make}, Model: {self.model}, Year: {self.year}, Color: {self.color}")
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

    def accelerate(self, increase):
        self.speed += increase
        if self.speed > 120:
            raise OverSpeedError(f"Speed limit exceeded! Current speed: {self.speed}")
        print(f"Accelerated by {increase} mph. Current speed: {self.speed}")

    def read_color_from_file(self, file_path):
        try:
            with open(file_path, "r") as file:
                self.color = file.read().strip()
            print(f"Car color read from file: {self.color}")
        except FileNotFoundError:
            print(f"Error: The file '{file_path}' was not found.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

my_car = Car("Toyota", "Corolla", 2022, 10)

my_car.read_color_from_file("color.txt")

my_car.print_car_info()
