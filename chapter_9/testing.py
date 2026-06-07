# Imports the specicic class from the car.py file.

from car import Car
from car import ElectricCar
from collections import OrderedDict

# Or we could use * to import them all.

my_new_car = Car('Audi', 'A4', 2016)
print(my_new_car.get_descriptive_name())

my_new_car.odometer_reading = 23
my_new_car.read_odometer()

my_new_car_2 = ElectricCar('Telsa', 'Model S', 2026)
my_new_car_2.describe_battery()

favourite_languages = OrderedDict()

favourite_languages['Steve'] = 'Python'
favourite_languages['Dave'] = 'Haskell'
favourite_languages['Brian'] = 'Go'
favourite_languages['Phil'] = 'C++'

for name, language in favourite_languages.items():
    print(name.title() + "'s favourite language is "
    "" + language.title() + ".")