class Car:
    """A simple attempt to respresent a car"""

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a neatly formated descriptive name"""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    def read_odometer(self):
        """Print a statement showing the car's mileage"""
        print(f"The car has {self.odometer_reading} miles on it. ")
    
    def update_odometer(self,mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You cannot roll back an odometer! ")
    
    def increment_odometer(self, miles):
        "Add the given amount to the odometer reading."
        self.odometer_reading+=miles
    
    def fill_gas_tank(self):
        print("We are filling the gas tank")
#modify attribute's value directly


class ElectricCar(Car):
    def __init__(self,make,model,year):
        super().__init__(make,model,year)
        self.battery_size = 40
        self.battery = Battery(65)
    
    def describe_battery(self):
        print(f"This car has a {self.battery_size}-kwh battery.")
    
    def fill_gas_tank(self):
        print("There is no reason to fill the gas")

class Battery:
    """A simple attempt to mdel a battery for an electric car."""

    def __init__(self, battery_size = 40):
        self.battery_size = battery_size

    def describe_battery(self):
        print(f"This car has a {self.battery_size} - kWh battery.")

    def get_range(self):
        if self.battery_size == 40:
            range = 150
        elif self.battery_size == 65:
            range = 225
        
        print(f"This car can about {range} miles on a full charge")

my_leaf = ElectricCar('nissan', 'leaf', 2024)
print(my_leaf.get_descriptive_name())

my_leaf.describe_battery()
my_leaf.fill_gas_tank()
my_leaf.battery.describe_battery()

my_leaf.battery.get_range()





