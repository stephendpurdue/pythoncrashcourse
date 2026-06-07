from collections import OrderedDict

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
    'dylan': ['1', '2', '4'],
    'george': ['2', '5', '4'],
    'stephen': ['4', '3', '4'],
    'phil': ['7', '3', '5'],
    'brian': ['2', '1', '6'],
}

# Sorted into alphabetical order.
for name, number in favourite_numbers.items():
    for numbers in number:

        print(favourite_numbers['dylan'])
        print(favourite_numbers['george'])
        print(favourite_numbers['stephen'])
        print(favourite_numbers['phil'])
        print(favourite_numbers['brian'])

# 6-3 + 6-4
glossary = OrderedDict()

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
    print(key.title() + ": " +  value.title())


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
    for language in favorite_languages:
        if name in favorite_languages:
            print('Thank you for responding')
        else:
            print('You should take the survey!')


# 6-7

persons = {
    'spurdue': {
        'first': 'stephen',
        'last': 'purdue',
        'location': 'uk'
    },

    'bobama': {
        'first': 'barrack',
        'last': 'obama',
        'location': 'usa'
    },

    'emacron': {
        'first': 'emmanuel',
        'last': 'macron',
        'location': 'france'
    }
}

for name, info in persons.items():
    print('Username: ' + name)
    full_name = info['first'] + " " + info['last']
    location = info['location']

    print('Full Name: ' + full_name)
    print('Location: ' + location)

# 6-8

pets = {
    'momo': {
        'type': 'cat',
        'owner': 'stephen'
    },

    'binx': {
        'type': 'cat',
        'owner': 'stephen'
    },

    'woody': {
        'type': 'dog',
        'owner': 'hugo'
    },

    'tilly': {
        'type': 'dog',
        'owner': 'dylan'
    }
}

for name, info in pets.items():
    print('Name: ' + name.title())
    type = info['type']
    owner = info['owner']
    
    print('Type:' + type.title())
    print('Owner:' + owner.title())


# 6-9

favourite_places = {
    'stephen': 'wyoming',
    'dylan': 'france',
    'george': 'vegas',
    'eric': 'bed'
}

for name, location in favourite_places.items():
    print(name + ' likes going to ' + location)


# 6-11

cities = {
    'New York': {
        'country': 'USA',
        'population': '8.8 million',
        'fact': 'The Statue of Liberty is here.'
    },

    'Southampton': {
        'country': 'UK',
        'population': '259,000',
        'fact': 'The Titanic left from here.'
    },

    'London': {
        'country': 'UK',
        'population': '9.2 million',
        'fact': 'Parliament is here.'
    }
}

for name, info in cities.items():
    print('City: ' + name)

    country = info['country']
    population = info['population']
    fact = info['fact']

    print(name + ' is in the ' + country + ' it has a population of ' + population + '. Here is an interesting fact: ' + fact)  