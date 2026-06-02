# Define the function, then print a string.
def say_hello(username):
    print("Hello " + username.title() + "!")

say_hello('stephen')

# A default value could be set to one of these variables, this would override the input.
def describe_knife(knife_type, price):
    print("I have a " + knife_type + " knife.")
    print("It cost me " + price + ".")

# Without keyword arguments
describe_knife("Japanese", "£114.99")
describe_knife("German", "£300")

# With keyword arguments
describe_knife(knife_type="Japanese", price="£114.99")
describe_knife(knife_type="German", price="£300")


# This takes two arguments, and then pops a value from uncooked_food and assigns it to current_recipe
# It is then added to the cooked food list
def make_food(uncooked_food, cooked_food):
    while uncooked_food:
        current_recipe = uncooked_food.pop()

        print('Cooking food: ' + current_recipe)
        cooked_food.append(current_recipe)

# This then prints the new cooked_food list
def show_cooked_food(cooked_food):
    print("\nThe following recipes have been cooked: ")
    for food in cooked_food:
        print(cooked_food)

# Define both the lists
uncooked_food = ['Burger', 'Fries', 'Ragu']
cooked_food = []

make_food(uncooked_food, cooked_food)
show_cooked_food(cooked_food)