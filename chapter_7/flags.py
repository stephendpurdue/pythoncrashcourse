# Set the prompts
prompt = 'Tell me something about yourself: '
prompt += "\nEnter 'quit' to end the program "

# Set the flag to True
active = True

# Loop through while active
while active:
    message = input(prompt)

# If message is quit, deactivate
    if message == 'quit':
        active = False
    elif message == 'admin':
        break
    else:
        print(message.title())

    