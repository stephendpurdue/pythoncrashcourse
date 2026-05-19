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

requested_cake = 'Chocolate', 'Victoria Sponge'

if requested_cake != 'Madeira':
    print('I do not like Madeira, Chocolate instead please!')
if 'Chocolate' in requested_cake:
    print('We have Chocolate!')
if 'Madeira' not in requested_cake:
    print('We have ran out of Madiera, sorry!')
if 'Victoria Sponge' in requested_cake:
    print('We have Victoria Sponge too!')

# Numerical comparisons

age = 10

if age != 50:
    print('You are too young!')

# Checking multiple conditions

age_1 = 18
age_2 = 21

if age_1 >= 21 and age_2 <= 21:
    print('You are old enough to drink!')


new_age = 19

if new_age >=18:
    print('You can vote!')
    print('Have you registered to vote?')
    print('Who are you voting for?')
else:
    print('You are not old enough to vote!')