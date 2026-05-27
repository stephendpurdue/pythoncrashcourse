# 7-1

rental = input('What type of car would you like? ')

if rental == 'Subaru':
    print('Let me see if there is one in stock! ')
elif rental == 'Volkswagen':
    print('I think we have one!')
else:
    print('We do not sell those unfortunately! ')


# 7-2

restaurant = input('How many of you are dining this evening? ')

restaurant = int(restaurant)
if restaurant >= 8:
    print('You will have to wait for a table, we are extremely busy! ')
else:
    print('Sure! Come on through! ')


# 7-3

multiples = input('Enter a number: ')

multiples = int(multiples)

if multiples % 10 == 0:
    print('It is a multiple of 10 ')
else:
    print('It is not a multiple of 10 ')