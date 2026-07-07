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


    def view(self):
        print("Test - View")

    def add(self):
        print("Test - Add")

    def new(self):
        print("Test - New")

    def exit(self):
        print("Test - Exit")

Main().main_menu()


