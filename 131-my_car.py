from ImportCarClass import Car

my_car= Car("audy","a4", 2024)
print(my_car.get_descriptive_name())

my_car.odometer_reading=400
my_car.read_odometer()