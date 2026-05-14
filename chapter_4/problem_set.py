# 4-1

pizzas = ['Margarita', 'Pepperoni', 'Capricossa', 'Milano']
for pizza in pizzas:
    print('I like ' + pizza + 'pizza!')

print('I really like pizza!')

# 4-2

animals = ['Dog', 'Cat', 'Parrot', 'Fish']
for animal in animals:
    print('A ' + animal + ' Would make a great pet!')

print('A Dog would be great to have with a cat!')

# 4-3

for num in range(1, 21):
    print(num)
    pass

# 4-4

million = []
for i in range(1, 1000000):
    million.append(i)
    pass

# 4-5

sum_million = [1, 1000000]
for num in range(1, 1000000):
    sum_million.append(num)
    min(sum_million)
    max(sum_million)
    pass

# 4-6

odd_numbers = list(range(1,21,3))
for i in odd_numbers:
    print(i)

# 4-7

threes = [value**3 for value in range(1, 30)]
print(threes)

