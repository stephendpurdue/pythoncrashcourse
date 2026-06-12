# 11-1 + 11-2

def cities(city, country, population):
    return(f"{city.title()}, {country.title()}, {population}")

cities('Southampton', 'UK', 231000)

# 11-3

class Employee():

    def __init__(self, first_name, last_name, annual_salary):
        self.first_name = first_name
        self.last_name = last_name
        self.annual_salary = annual_salary

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}" # f string is cleaner.

    def give_default_raise(self, increase=5000):
        self.annual_salary += increase # Modifies the salary in place so it can be reused later.
        return self.annual_salary

    def give_custom_raise(self, custom_increase):
        self.annual_salary += custom_increase
        return self.annual_salary

    def print_employee_information(self):
        print(self.get_full_name())
        print(self.annual_salary)
 

Employee('Stephen', 'Purdue', 30000).give_default_raise(5000)
Employee('Stephen', 'Purdue', 30000).print_employee_information()
