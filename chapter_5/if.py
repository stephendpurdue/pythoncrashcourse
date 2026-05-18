cakes = ['Madeira', 'Chocolate', 'Victoria Sponge']

for cake in cakes:
    if cake == 'Chocolate':
        print(cake.lower())
    else:
        print(cake.title())

new_cake = 'Battenburg'

if new_cake not in cakes:
    print('Battenburg: This one is not very popular')

# Make sure to put brackets when using methods within if statements, else it will print an error.

requested_cake = 'Chocolate'

if requested_cake != 'Madeira':
    print('I do not like Madeira, Chocolate instead please!')

# Numerical comparisons

age = 10

if age != 50:
    print('You are too young!')

# Checking multiple conditions

age_1 = 18
age_2 = 21

if age_1 >= 21 and age_2 <= 21:
    print('You are old enough to drink!')
