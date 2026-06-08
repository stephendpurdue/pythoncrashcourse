# 10-1

with open('learning_python.txt') as file_object:
    contents = file_object.read()
    print(contents)

with open('learning_python.txt') as file_object_2:
    for line in file_object_2:
        print(line.rstrip())

filename = 'learning_python.txt'

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

guest_file = 'guest_book.txt'


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

    with open('info.txt', 'a') as r:
        r.write(reason.title() + '\n')