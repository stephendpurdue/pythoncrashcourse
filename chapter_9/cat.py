class Cat():

    def __init__(self, name, age, miles):
        self.name = name
        self.age = age
        self.miles = miles

    def sit(self):
        print(self.name.title() + " is now sitting.")

    def roll_over(self):
        print(self.name.title() + " rolled over!")

    def mileage(self, miles):
        print('The cat currently has: ' + self.miles + ' miles.')

my_cat = Cat('Mo Mo', 13, 2500)
your_cat = Cat('Phil', 15, 2300)

print("My cat's name is  " + my_cat.name.title() + ".")
print("My cat is " + str(my_cat.age) + " years old.")
print("My cat has done " + str(my_cat.miles) + " miles!")

print("Your cat's name is  " + your_cat.name.title() + ".")
print("Your cat is " + str(your_cat.age) + " years old.")
print("Your cat has done " + str(your_cat.miles) + " miles!")

question = input('Should Mo Mo sit? yes/no ')
if question.lower() == 'yes':
    my_cat.sit()
else:
    my_cat.roll_over()



class ChomkChart(Cat):

    def __init__(self, name, age, miles):
        super().__init__(name, age, miles)

    def chart(self):
        question_2 = input(
            "Enter your cats weight in percentage of body fat, " # This is better formatting for strings.
            "and I will tell you their chonk scale! "
        )
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

my_question = ChomkChart("Binx", 18, 5000) # Has to recieve arguments as it has inherited from Cat()
my_question.chart()