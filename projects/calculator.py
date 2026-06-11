
class Calculator():

    def initialise(self):
        operation = str(input("Please enter your desired operation: "
            "(+ / - / * / or /), or enter 'q' to quit. "))
        
        if operation == '+':
            self.addition()
        elif operation == '-':
            self.subtraction()
        elif operation == '*':
            self.multiplication()
        elif operation == '/':
            self.division()
        else:
            print("Unsupported operation type.")
            self.initialise()

    def addition(self):
        num1 = int(input("Please enter a number: "))
        num2 = int(input("Please enter another number: "))
        print(num1 + num2)

    def subtraction(self):
        num1 = int(input("Please enter a number: "))
        num2 = int(input("Please enter another number: "))
        print(num1 - num2)

    def multiplication(self):
        num1 = int(input("Please enter a number: "))
        num2 = int(input("Please enter another number: "))
        print(num1 * num2)


    def division(self):
        num1 = int(input("Please enter a number: "))
        num2 = int(input("Please enter another number: "))
        print(num1 / num2)

Calculator().initialise()