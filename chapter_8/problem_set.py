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

# 8-7

def make_album(artist_name, album_title):
    album = {'name': artist_name, 'title': album_title}
    return album

new_album_1 = make_album('Runaway', 'Bonjovi')
new_album_2 = make_album('Apologise', 'One Republic')
new_album_3 = make_album('CTRL ESCAPE', 'John Summit')
print(new_album_1, new_album_2, new_album_3)