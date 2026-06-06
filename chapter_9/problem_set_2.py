# 9-6

class Restaurant():

    def __init__(self, restaurant_name, cuisine_type, total_customers):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.location = 'Romsey' # This is a default value
        self.customers = total_customers
        self.number_served = 0

    def describe_restaurant(self):
        print("Hello! Welcome to " + self.restaurant_name +  ", we serve " 
              + self.cuisine_type + " cuisine." 
              + " It is located in " + self.location + '.')

    def open_restaurant(self):
        print("Come on in, we are open!")

    def set_number_served(self, total_customers):
        self.number_served = total_customers
        print("We have served " 
              + str(self.number_served) + " people.")

    def update_number_served(self, additional_customers):
        self.number_served += additional_customers
        print("We have now served " 
              + str(self.number_served) + " people.")

# 1. Define the subclass
# 2. Call the constructor
# 3. Call its methods

class IceCreamStand(Restaurant):

    def __init__(self, restaurant_name, cuisine_type, total_customers):
        super().__init__(restaurant_name, cuisine_type, total_customers)

    def types(self, flavours=['Vanilla', 'Chocolate', 'Strawberry']):
        self.flavours = flavours
        print("We have these flavours of ice cream: " + str(self.flavours))

icecreamstand = IceCreamStand('Lattimers', 'Modern', 200)
icecreamstand.types()