class Cat():

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sit(self):
        print(self.name.title() + " is now sitting.")

    def roll_over(self):
        print(self.name.title() + " rolled over!")

my_cat = Cat('Mo Mo', 13)
your_cat = Cat('Phil', 2)

print("My cat's name is  " + my_cat.name.title() + ".")
print("My cat is " + str(my_cat.age) + " years old.")

print("Your cat's name is  " + your_cat.name.title() + ".")
print("Your cat is " + str(your_cat.age) + " years old.")

question = input('Should Mo Mo sit? yes/no ')
if question.lower() == 'yes':
    my_cat.sit()
else:
    my_cat.roll_over()

# The Chomnk Chart    

question_2 = input("Enter your cats weight in percentage of body fat, and I will tell you their chonk scale! ")
question_2 = int(question_2)

if question_2 <= 20:
    print('A Fine Boi')
elif question_2 <= 30:
    print('He Chomnk')
elif question_2 <= 40:
    print("A Heckin' Chonker")
elif question_2 <= 50:
    print('HEFTYCHONK')
elif question_2 <= 60:
    print('MEGACHONKER')
else:
    print('OH LAWD HE COMIN!')
