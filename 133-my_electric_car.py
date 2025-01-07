from MultiClassModule import ElectricCar
from MultiClassModule import ElectricCar, Car


my_leaf = ElectricCar("nissan", "leaf", 2024)
print(my_leaf.get_descriptive_name())
my_leaf.battery.describe_battery()
my_leaf.battery.get_range()

my_car= Car("Toyota","a4", 1999)
print(my_car.get_descriptive_name())

#It's possible to import module in to a module...........