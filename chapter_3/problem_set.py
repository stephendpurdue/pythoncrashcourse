# 3-1

names = ['Dylan', 'George', 'Ben']

print(names[0])
print(names[1])
print(names[2])


# 3-2

message_1 = 'You have a nice car ' + names[0] + '.'
message_2 = 'You have a nice house ' + names[1] + '.'
message_3 = 'You have a nice snowboard ' + names[2] + '.'

print(message_1)
print(message_2)
print(message_3)


# 3-3

cars = ['Volkswagen', 'BMW', 'Audi', 'Honda', 'Jaguar', 'Lamborghini']

car_message = 'I would like to own a nice ' + cars[0] + '.'
car_message_2 = 'I love driving my ' + cars[1] + '.'

print(car_message)
print(car_message_2)

# Modifying and appending existing list

cars[0] = 'Range Rover'
print(cars)

cars.append('Vauxhall')
print(cars)

cars_2 = []

cars_2.append('Tesla')
cars_2.append('Porsche')
cars_2.append('Ferarri')

cars_2.insert(1, 'Honda')
del cars_2[0]

print(cars_2)


# .pop()

popped_cars = cars_2.pop()
print(cars_2)
print(popped_cars)

last_owned = cars_2.pop(1)
print('The last car I owned was a ' + last_owned.title() + '.')


# 3-4

guest_list = ['Bill Gates', 'King Charles III', 'Elon Musk']

print('You are invited to dinner ' + guest_list[0] + '.')
print('You are invited to dinner ' + guest_list[1] + '.')
print('You are invited to dinner ' + guest_list[2] + '.')

print(len(guest_list))


# 3-5

print('It is unfortunate you cannot come ' + guest_list[0] + '.')

guest_list[0] = 'Sam Altman'

print('You are invited to dinner ' + guest_list[0] + '.')
print('You are invited to dinner ' + guest_list[1] + '.')
print('You are invited to dinner ' + guest_list[2] + '.')

# 3-6

print('We have found a new table table, suitable for three more guests')

guest_list.insert(0, 'Jensen Huang')
guest_list.insert(2, 'Yann Le Cun')
guest_list.append('Joe Rogan')

print('You are invited to dinner ' + guest_list[0] + '.')
print('You are invited to dinner ' + guest_list[1] + '.')
print('You are invited to dinner ' + guest_list[2] + '.')
print('You are invited to dinner ' + guest_list[3] + '.')
print('You are invited to dinner ' + guest_list[4] + '.')
print('You are invited to dinner ' + guest_list[5] + '.')

# 3-7

print('The table will not arrive in time, there is only room for two people.')

guest_list.pop()
print('I am sorry I cannot invite you to dinner, hopefully there will be room next time.')

guest_list.pop()
print('I am sorry I cannot invite you to dinner, hopefully there will be room next time.')

guest_list.pop()
print('I am sorry I cannot invite you to dinner, hopefully there will be room next time.')

guest_list.pop()
print('I am sorry I cannot invite you to dinner, hopefully there will be room next time.')

print('You are still invited! ' + guest_list[0])
print('You are still invited! ' + guest_list[1])

del guest_list[0]
del guest_list[0]

print(guest_list) 


# 3-8

locations = ['Las Vegas', 'Thailand', 'Wyoming', 'Oregon', 'Switzerland']

print(locations)
print(sorted(locations))
print(locations)

print(sorted((locations)))

locations.reverse()
print(locations)

locations.reverse()
print(locations)

locations.sort()
print(locations)