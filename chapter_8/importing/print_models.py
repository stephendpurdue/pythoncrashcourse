import printing_functions # Import a file
from printing_functions import make_car # Import a specific function without an alias
from printing_functions import make_car as mc # Import a specific function with an alias
import printing_functions as pf # Import a file with an alias
from printing_functions import * # Import all functions in the file

car = printing_functions.make_car('Volkswagen', 'Polo', color='Ascot Grey', tow_package=False)
car_2 = printing_functions.make_car('BMW', 'A2', color='Jet Black', tow_package=False)
print(car, car_2)