from random import randint

class Die():

    def __init__(self, num_sides=6):
        """Set the number of sides"""
        self.num_sides = num_sides

    def roll(self):
        """Return a random integer between 1 and the number of sides"""
        return randint(1, self.num_sides)
    

Die().roll()