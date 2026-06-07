from user_data import User

class Admin(User): # To inherit, it must be passed the other class.
    
    def __init__(self, first_name, last_name): # The super() method initializes the value of the inherited class.
        super().__init__(first_name, last_name)

    def describe_admin(self):
        print('An admin user has full control over the system.')


# 9-8

class Privileges(Admin):

     def describe_privileges(self):
        print("\nAdmin users can do the following: " 
              + "\nMake posts" 
              + "\nBan users" 
              + "\nEdit system settings") 