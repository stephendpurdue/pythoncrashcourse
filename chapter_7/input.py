message = input("Give me an answer, and I'll repeat it back:")
if message == 'Cake':
    print('That is cool!')
print(message)

prompt = "If you like cake, you should tell us! "
prompt += "\nDo you like cake? "

question = input(prompt)

if question == 'Yes':
    print('I knew it!')
else:
    print('That is a real shame!')

# Takes an input
number = input('Enter a number:')

# Converts from str to int
number = int(number)

# Checks if number is divisible by two, then prints a statement
if number % 2 == 0:
    print('The number is even.')
else:
    print('The number is odd.')

# Declare a number 
current_number = 2 
# Start the loop
while current_number <= 10:
    print(current_number)
    # Increment by one
    current_number += 1