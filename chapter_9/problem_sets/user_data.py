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



