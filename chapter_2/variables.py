# Variables can be assigned strings etc, and then called in another funtion, this example uses the print function.
message_1 = "I love Tomorrowland!"
print(message_1)

# Changing case in string methods.

message_2 = "I'm learning python!"
print(message_2.upper())
print(message_2.lower())
print(message_2.title())

# String concatenation.
# \n can be used for a new line.

full_string = message_1 + " " + message_2
print(full_string)

print("Hello, " + message_1.title() + "\n!")

name = "Stephen "
print(name.strip())