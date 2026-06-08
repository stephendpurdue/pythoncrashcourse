import json

# 10-1

with open('files/learning_python.txt') as file_object:
    contents = file_object.read()
    print(contents)

with open('files/learning_python.txt') as file_object_2:
    for line in file_object_2:
        print(line.rstrip())

filename = 'files/learning_python.txt'

with open(filename) as file_object_3:
    lines = file_object_3.readlines()
    for line in lines:
        line.replace('python', 'C')

for line in lines:
    print(line.rstrip())

# 10-2

with open(filename) as f:
    text = f.read()

text = text.replace('python', 'C')
print(text)

# 10-3 + 10-4

guest_file = 'files/guest_book.txt'


while True:
    print("Welcome!")
    print("Type 'quit' to exit the interface ")
    name = input("Please enter your name: ")

    if name.lower() == 'quit':
        print("Goodbye!")
        break

try:
    with open(guest_file, 'a') as g:
        g.write(name.title() + '\n')
except FileNotFoundError:
    print('The file ' + guest_file + " does not exist.")

# 10-5

while True:
    print("Type 'quit' to exit the interface ")
    reason = input("Why do you like programming? ")

    if reason.lower() == 'quit':
        break

    with open('files/info.txt', 'a') as r:
        r.write(reason.title() + '\n')

# 10-6 + 10-7

def calculation():
    while True:
        try:
            raw_1 = input("Enter a number: ") # Takes in two inputs and checks for an exit clause:
            if raw_1.lower() == 'quit':
                break
            raw_2 = input("Enter another number: ")
            if raw_2 == 'quit':
                break

            number_1 = int(raw_1) # Converts them to integers
            number_2 = int(raw_2)

        except ValueError: # Checks for erros
            print("That isn't a number, please use integers only")       
        else:
            sum = number_1 + number_2 # Prints the total
            print("Total: ", sum)

calculation()

# 10-8 + 10-9

def read_files(filename):
    try:
        with open(filename) as file_obj:
            contents = file_obj.read()
    except FileNotFoundError:
        pass
    else:
        print(contents)

filenames = 'files/cats.txt', 'files/dogs.txt'
for filename in filenames:
    read_files(filename)

# 10-10

def count_word(filename_2):
    try:
        with open(filename_2) as f:
            text = f.read()
            count_the = text.lower().count('the')
            print(count_the)
    except FileNotFoundError:
        print("File not found: ", filename_2)

filename_2 = 'files/projectgutenberg.txt'
count_word(filename_2)

