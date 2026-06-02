def make_car(manufacturer, model, **info):
    cars = {}
    cars['manufacturer'] = manufacturer
    cars['model'] = model
    for key, value in info.items():
        cars[key] = value
    return cars

car = make_car('Volkswagen', 'Polo', color='Ascot Grey', 
               tow_package=False)
car_2 = make_car('BMW', 'A2', color='Jet Black', 
                 tow_package=False)
print(car, car_2)