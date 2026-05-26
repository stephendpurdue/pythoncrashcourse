# 6-1

person = {
    'first_name': 'Dylan',
    'last_name': 'Sullivan',
    'age': '21',
    'city': 'Southampton'
}

print(person['first_name'])
print(person['last_name'])
print(person['age'])
print(person['city'])

# 6-2

favourite_numbers = {
    'dylan': '5',
    'george': '8',
    'stephen': '7',
    'phil': '3',
    'brian': '1'
}

# Sorted into alphabetical order.
for name, number in sorted(favourite_numbers.items()):
    print(name)

print(favourite_numbers['dylan'])
print(favourite_numbers['george'])
print(favourite_numbers['stephen'])
print(favourite_numbers['phil'])
print(favourite_numbers['brian'])

# 6-3 + 6-4

glossary = {
    'Dictionaries': 'are a useful tool to store and then access information.',
    'Lists': 'are a useful tool to store and then access information, they can be looped through.',
    'Classes': 'are a useful tool to order and structure funtions & data',
    'If statements': 'are a useful tool to compare values and run checks, they follow the if, elif, else format.',
    'Looping': 'this involves repeating through a list or dictionary etc.',
    'Integers': 'are numbers',
    'Strings': 'are characters',
    'Booleans': 'are True or False'
}

for key, value in glossary.items():
    print(key, value)


# 6-5

rivers = {
    'Nile': 'Egypt',
    'Missisipi': 'USA',
    'Thames': 'UK'
}

for key, value in rivers.items():
    print('The ' + key + ' runs through ' + value)
    print(key)
    print(value)


# 6-6

favorite_languages = {    
    'jen': 'python',    
    'sarah': 'c',    
    'edward': 'ruby',    
    'phil': 'python',    
}

names = ['jen', 'dave', 'phil', 'edward', 'steve']

for name in names:
    for language in favorite_languages.items():
        if name in favorite_languages:
            print('Thank you for responding')
        else:
            print('You should take the survey!')