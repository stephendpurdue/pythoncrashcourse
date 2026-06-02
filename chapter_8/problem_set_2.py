# 8-9

def magicians(new_magicians):
    for magician in new_magicians:
        print(magician)

new_magicians = ['Dave', 'Brian', 'Phil', 'Dumbledore']

magicians(new_magicians)

# 8-10 + 8-11

def great_magicians(new_magicians):
    for magician in new_magicians:
        print(magician[:] + ' the Great')

great_magicians(new_magicians)
magicians(new_magicians)

# 8-12

def make_sandwich(*fillings):
    for filling in fillings:
        print("Your sandwich contains: " + filling + '.')

make_sandwich('Ham', 'Cheese', 'Mayo')
make_sandwich('Cheese', 'Pickle')
make_sandwich('Bacon', 'Lettuce', 'Tomato')

# 8-13

def build_profile(first, last, **user_info):
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile

user_profile = build_profile('albert', 'einstein',
                             location='princeton',
                             field='physics')

user_profile_2 = build_profile('stephen', 'purdue',
                             location='winchester',
                             field='game development')

print(user_profile, user_profile_2)

# 8-14

# This function takes two default arguments, and an unspecified amount of arbitrary arguments
# An empty dictionary is initialise, with the key and value pair being set, the items are then accessed and returned.
def make_car(manufacturer, model, **info):
    cars = {}
    cars['manufacturer'] = manufacturer
    cars['model'] = model
    for key, value in info.items():
        cars[key] = value
    return cars

car = make_car('Volkswagen', 'Polo', color='Ascot Grey', tow_package=False)
car_2 = make_car('BMW', 'A2', color='Jet Black', tow_package=False)
print(car, car_2)