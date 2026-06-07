from restaurant import Restaurant # This imports the class from a module in another folder
from user_data import User
from admin_data import Admin, Privileges

# 9-10

new_restaurant = Restaurant('Cinder', 'Modern', 300)
new_restaurant.describe_restaurant()

# 9-11 + 9-12

new_user = Privileges('Stephen', 'Purdue')
new_user.describe_privileges()

new_user = Privileges('Stephen', 'Purdue')
new_user.describe_privileges()