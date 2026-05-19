# 5-1 

car = 'BMW'
print("\nIs car == 'BMW'? I predict True.")
print(car == 'BMW')

car = 'Volkswagen'
print("\nIs car == 'Volkswagen'? I predict True.")
print(car == 'Volkswagen')

car = 'Skoda'
print("\nIs car == 'Volkswagen'? I predict False.")
print(car == 'Volkswagen')

car = 'BMW'
print("\nIs car == 'Audi'? I predict False.")
print(car == 'Audi')

car = 'BMW'
print("\nIs car == 'Skoda'? I predict False.")
print(car == 'Skoda')

car = 'Skoda'
print("\nIs car == 'BMW'? I predict False.")
print(car == 'BMW')

car = 'BMW'
print("\nIs car == 'BMW'? I predict True.")
print(car == 'BMW')

car = 'Skoda'
print("\nIs car == 'Volkswagen'? I predict False.")
print(car == 'Volkswagen')

car = 'Toyota'
print("\nIs car == 'Toyota'? I predict True.")
print(car == 'Toyota')

car = 'Toyota'
print("\nIs car == 'Volkswagen'? I predict False.")
print(car == 'Volkswagen')

# 5-2

car = 'BMW'
print("\nIs car == 'Volkswagen'? I predict False.")
print(car.lower() == 'Volkswagen')

amount_of_people = 5

if amount_of_people >= 4:
    print('Busy!')

if amount_of_people != 6:
    print('Not that busy!')

cake = ['Chocolate', 'Battenburg']
other_cakes = 'Madeira', 'Victoria Sponge'

if other_cakes not in cake:
    print('It has to be chocolate!')

if other_cakes in cake:
    print('It is there!')

# 5-3

alien_colour = ['green', 'yellow', 'red']

for colour in alien_colour:
    if colour == 'green':
        print('You earned 5 points!')
    elif alien_colour == 'blue':
        print('You earned 10 points!')
    else:
        print('No points for you!')