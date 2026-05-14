# 4-8 / 4-9

cubes = [value**3 for value in range(1,10)]
print(cubes)

# 4-10

names = ['Brian', 'Dave', 'Phil', 'Sharon', 'Brian', 'Dave', 'Phil', 'Sharon']
print(names[:3])
print(names[:-2])
print(names[:4])

# 4-11 / 12

pizzas = ['Margarita', 'Pepperoni', 'Capricossa', 'Milano']
friends_pizzas = pizzas[:] # Copy the list
pizzas.append('Texan Barbeqeue')
friends_pizzas.append('Calzone')

print('My favourite pizzas are: ')
for i in pizzas:
    print(i)

print('My friends favourite pizzas are: ')
for i in friends_pizzas:
    print(i)

# 4-13

buffet = ('Cake', 'Chicken', 'Sushi', 'Ice Cream', 'Fries')
for food in buffet:
    print(buffet)

new_buffet = ('Cake', 'Chicken', 'Sushi', 'Steak', 'Burgers')
for food in new_buffet:
    print(new_buffet)


