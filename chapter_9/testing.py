# Imports the specicic class from the car.py file.

from car import Car

my_new_car = Car('Audi', 'A4', 2016)
print(my_new_car.get_descriptive_name())

my_new_car.odometer_reading = 23
my_new_car.read_odometer()