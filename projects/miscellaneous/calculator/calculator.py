class Calculator():

    # Core logic
    def add(self, a, b):
        return a + b
    
    def subtract(self, a, b):
        return a - b
    
    def multiply(self, a, b):
        return a * b
    
    def divide(self, a, b):
        return a / b
    
    # Initialisation
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

    # Printed logic (user-facing)
    def addition(self):
        num1 = int(input("Please enter a number: "))
        num2 = int(input("Please enter another number: "))
        print(self.add(num1, num2))

    def subtraction(self):
        num1 = int(input("Please enter a number: "))
        num2 = int(input("Please enter another number: "))
        print(self.subtract(num1, num2))

    def multiplication(self):
        num1 = int(input("Please enter a number: "))
        num2 = int(input("Please enter another number: "))
        print(self.multiply(num1, num2))


    def division(self):
        num1 = int(input("Please enter a number: "))
        num2 = int(input("Please enter another number: "))
        print(self.divide(num1, num2))

Calculator().initialise()