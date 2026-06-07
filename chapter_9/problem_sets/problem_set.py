# 9-1, 9-2 + 9-4

class Restaurant():

    def __init__(self, restaurant_name, cuisine_type, total_customers):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.location = 'London' # This is a default value
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
        print("We have served " + str(self.number_served) + " people.")

    def update_number_served(self, additional_customers):
        self.number_served += additional_customers
        print("We have now served " + str(self.number_served) + " people.")
        

# 9-3 + 9-5

class User():
    
    def __init__(self, first_name, last_name, ):
        self.first_name = first_name
        self.last_name = last_name
        self.full_name = first_name + " " + last_name
        self.login_attempts = 0

    def describe_user(self):
        print("This users full name is: " + self.first_name + " " + self.last_name + ".")

    def greet_user(self):
        print("Greetings! " + self.full_name)

    def password(self, login_attempts=0):
        password = 'admin'.title()
        attempt = input('Please enter a password: ')
        if attempt == password:
            print('Login Successful!')
        else:
            self.login_attempts += 1
            print('Access Denied! Number of attempts: ' + str(self.login_attempts))

    def greet_admin(self):
        print('Greetings Admin! ' + self.full_name + '.')

user_1 = User('Stephen', 'Purdue')
user_1.describe_user()
user_1.greet_user()
user_1.password()

user_2 = User('Bill', 'Clinton')
user_2.describe_user()
user_2.greet_user()

user_3 = User('Michael', 'Jackson')
user_3.describe_user()
user_3.greet_user()

class Admin(User): # To inherit, it must be passed the other class.
    
    def __init__(self, first_name, last_name): # The super() method initializes the value of the inherited class.
        super().__init__(first_name, last_name)

    def describe_admin(self):
        print('An admin user has full control over the system.')


# 9-8

class Privileges(Admin):

     def describe_privileges(self):
        print("An admin can do the following: " 
              + "\nMake posts" 
              + "\nBan users" 
              + "\nEdit system settings") 

new_admin = Privileges('Stephen', 'Purdue')
new_admin.describe_admin()
new_admin.describe_privileges()