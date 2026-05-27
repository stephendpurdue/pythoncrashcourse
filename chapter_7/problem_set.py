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


# 7-4 

toppings = input('Enter a topping: ')
toppings += "\n Enter 'quit' to exit the store "

while True:
    pizza = input(toppings)

    if pizza == 'quit':
        break
    else:
        print("I'll add it to your pizza!")


# 7-5

tickets = input('How old are you? ')

age = int(tickets)

if age <= 3:
    print('Your ticket is free!')
elif age <= 12:
    print('Your ticket is £10')
elif age > 12:
    print('Your ticket is £15')
else:
    print('Your ticket is £20!')

# 7-7

x = 2
while x <= 5:
    print(x)
    x += 1
    pass


# 7-8 + 7-9 -> 7-8 (New Solution)

# Declare the list
sandwich_orders = ['Tuna', 'Pastrami', 'Cheese', 'Pastrami', 'BLT', 'Pastrami']
finished_sandwiches = []

# Loop through and remove Pastrami
while 'Pastrami' in sandwich_orders:
    sandwich_orders.remove('Pastrami')

# Ask for an input
order = input('What sandwich would you like? ')

# Loop through the list and check if the order is in the list, if so, add it to the new list
if order in sandwich_orders:
    print("I made your " + order + " sandwhich. ")
    finished_sandwiches.append(order)
else:
    print("We don't have that sandwhich I'm afraid! ")

# Print the finished list
print("Finished sandwhiches: ", finished_sandwiches)
print("We have run out of Pastrami!")

# 7-10

vacation = {}

polling_active = True

while polling_active:
    name = input("What is your name? ")
    response = input("What country would you like to go on vacation to? ")

    vacation[name] = response

    repeat = input("Should another person respond? ")
    if repeat == 'No':
        polling_active = False

print("<----RESULTS---->")

for name, response in vacation.items():
    print(name + ' would like to go to ' + response + '.')

