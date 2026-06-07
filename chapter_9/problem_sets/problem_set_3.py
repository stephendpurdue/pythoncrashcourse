from restaurant import Restaurant # This imports the class from a module in another folder
from user_data import User
from admin_data import Admin, Privileges
from random import randint
# 9-10

new_restaurant = Restaurant('Cinder', 'Modern', 300)
new_restaurant.describe_restaurant()

# 9-11 + 9-12

new_user = Privileges('Stephen', 'Purdue')
new_user.describe_privileges()

new_user = Privileges('Stephen', 'Purdue')
new_user.describe_privileges()

# 9-14
class Die():

    def __init__(self, sides):
        self.sides = sides

    def roll_die(self, times=10): # More compact version that uses List Comprehension
        return [randint(1, self.sides) for _ in range(times)]
        

die_1 = Die(6)
results = die_1.roll_die()

die_2 = Die(10)
results_2 = die_2.roll_die()

die_3 = Die(20)
results_3 = die_3.roll_die()

print(results)
print(results_2)
print(results_3)