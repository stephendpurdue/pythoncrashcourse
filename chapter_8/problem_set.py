# 8-1

def message():
    print('In this chapter, we are learning about functions, '
    'and how they can be applied in the wider context of Python programming.')

message()

# 8-2

def display_message(title):
    print("One of my favourite books is: " + title + ".")

display_message("The Courage to be Disliked")

# 8-3 & 8-4

def make_tshirt(size, message):
    print('You have ordered a ' + size + ' size tshirt, which has this written on it: ' + message + ' .')

make_tshirt(size='Small', message='I love cake')
make_tshirt('Large', 'I love Python')

# 8-5

def describe_city(name, location='UK'):
    print(name + ' is in ' + location)

describe_city('Reykjavik', 'Iceland')
describe_city('London', 'UK')
describe_city('New York', 'USA')

# 8-6

def city_country(city, country):
    print(city + ', ' + country + '.')

city_country('London', 'UK')