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