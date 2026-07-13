import json

# Create user inputs - DONE
# Add saved user inputs to a json file
# Save and retrieve

# The list will be added to a JSON file, and retrieved / written to when required.

class Main:

    def __init__(self):
        pass

    # Main Menu
    def main_menu(self):

        while True:
            print("\n---MENU---")
            print("1. View list")
            print("2. Add to list")
            print("3. Create a new list")
            print("4. Exit application")

            response = input("Enter desired function: ")

            if response == "1":
                Main().view()
            elif response == "2":
                Main().add()
            elif response == "3":
                Main().new()
            elif response == "4":
                break
            else:
                print("Unknown function. Please try again.")
                Main().main_menu()

    # File Viewer
    def view(self): 
        try:
            load = 'list.json'
            with open(load) as l_obj:
                words = json.load(l_obj)
                print(words)
        except FileExistsError:
            print("Sorry, that file doesn't exist. Returning to menu.")
            Main().main_menu()    

    # Add to a File
    def add(self): # Prompts user for input and writes it to the list.
        addition = input("Enter new list contents: ")
        current_list = 'list.json'
        with open(current_list, 'w') as cl:
            cl.write(addition)

    # Create a New File
    def new(self):
        
        data = input("Enter initial list contents: ")
        with open('list.json', 'w') as new_list:
            json.dump(data, new_list, indent = 4)
        

Main().main_menu()


