class Car():

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()
    
    def read_odometer(self):
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        self.odometer_reading += miles

class ElectricCar(Car):

    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery() # This should have brackets so it can turn into an instance.
        self.battery_size = 70

    def describe_battery(self):
        print("This car has a " + str(self.battery_size) + "-kWh battery.")

class Battery():
    
    def __init__(self, battery_size=70):
        self.battery_size = battery_size

    def get_range(self):
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270
        else:
            range = 0

        message = "This car can go approximately " + str(range)
        message += " miles on a full charge."
        print(message)

    # 9-9
    def upgrade_battery(self):
        if self.battery_size < 85:
            self.battery_size = 85
        else:
            print("This battery cannot be upgraded any further!")

my_tesla = ElectricCar('Tesla', 'Model S', '2026')

my_tesla.describe_battery() # Get initial info
my_tesla.battery.get_range() # Get the original range
my_tesla.battery.upgrade_battery() # Upgrade the battery
my_tesla.battery.get_range() # Check the new range