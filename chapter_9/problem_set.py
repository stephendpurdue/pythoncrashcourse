# 9-1 + 9-2

class Restaurant():

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print("Hello! Welcome to " + self.restaurant_name +  ", we serve " + self.cuisine_type + " cuisine.")

    def open_restaurant(self):
        print("Come on in, we are open!")

lattimers = Restaurant('Lattimers', 'Modern Contemporary')
lattimers.describe_restaurant()
lattimers.open_restaurant()

ennios = Restaurant('Ennios', 'Italian')
ennios.describe_restaurant()
ennios.open_restaurant()

strakers = Restaurant('Strakers', 'Modern Contemporary')
strakers.describe_restaurant()
strakers.open_restaurant()


class User():
    
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.full_name = first_name + " " + last_name

    def describe_user(self):
        print("This users full name is: " + self.first_name + " " + self.last_name + ".")

    def greet_user(self):
        print("Greetings! " + self.full_name)

user_1 = User('Stephen', 'Purdue')
user_1.describe_user()
user_1.greet_user()

user_2 = User('Bill', 'Clinton')
user_2.describe_user()
user_2.greet_user()

user_3 = User('Michael', 'Jackson')
user_3.describe_user()
user_3.greet_user()