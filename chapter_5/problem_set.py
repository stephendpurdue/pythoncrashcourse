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

# 5-4

new_alien_colour = 'Blue'

if new_alien_colour == 'Green':
    print('You just scored 5 points!')
else:
    print('You just scored 10 points!')

new_alien_colour_2 = 'Green'

if new_alien_colour_2 == 'Green':
    print('You just scored 5 points!')
else:
    print('You just scored 10 points!')

# 5-5

final_alien_colour = 'Green'

if final_alien_colour == 'Green':
    print('You just scored 5 points!')
elif final_alien_colour == 'Yellow':
    print('You just scored 10 points!')
else:
    print('You just scored 15 points!')

final_alien_colour = 'Yellow'

if final_alien_colour == 'Green':
    print('You just scored 5 points!')
elif final_alien_colour == 'Yellow':
    print('You just scored 10 points!')
else:
    print('You just scored 15 points!')

final_alien_colour = 'Red'

if final_alien_colour == 'Green':
    print('You just scored 5 points!')
elif final_alien_colour == 'Yellow':
    print('You just scored 10 points!')
else:
    print('You just scored 15 points!')


# 5-6

age = 20

if age <= 2:
    print('This person is a baby')
elif age <= 4:
    print('This person is a toddler')
elif age <= 13:
    print('This person is a kid')
elif age <= 20:
    print('This person is a teenager')
elif age <= 65:
    print('This person is an adult')
else:
    print('This person is an elder')

# 5-7

favourite_fruits = ['Banana', 'Mango', 'Peach']

for fruit in favourite_fruits:
    if fruit == 'Banana':
        print('You like bananas!')
    elif fruit == 'Kiwi':
        print('You like Kiwi!')
    elif fruit == 'Mango':
        print('Mangos are cool!')
    elif fruit == 'Peach':
        print('Peaches are awesome!')
    elif fruit == 'Apple':
        print('Apples are cool too I guess')
    else:
        print('What other fruit do you like?')

# 5-8 + 5-9

usernames = ['Stephen']

for name in usernames:
    if name == 'Admin':
        print('Hello Admin.')
    elif name in usernames:
        print('Hello ' +  name + '. Thank you for logging in again.')
    else:
        print('We need to find some users!')


# 5-10

current_users = ['Dave', 'Phil', 'Brian', 'Andy', 'Mike']
new_users = ['Stephen', 'Dylan', 'George', 'Phil', 'Randy']

for user in new_users:
    if user in current_users:
        print('That name is already taken!')
    else:
        print('That name is available!')

# 5-11

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for number in numbers:
    if number == 1:
        print('1st')
    elif number == 2:
        print('2nd')
    elif number == 3:
        print('3rd')
    elif number == 4:
        print('4th')
    elif number == 5:
        print('5th')
    elif number == 6:
        print('6th')
    elif number == 7:
        print('7th')
    elif number == 8:
        print('8th')
    elif number == 9:
        print('9th')