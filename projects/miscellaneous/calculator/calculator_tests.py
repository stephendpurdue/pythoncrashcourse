import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def test_addition(self):
        calc = Calculator()
        result = calc.add(17, 20)
        self.assertEqual(result, 37)

    def test_subtraction(self):
        calc = Calculator()
        result = calc.subtract(20, 10)
        self.assertEqual(result, 10)

    def test_multiplication(self):
        calc = Calculator()
        result = calc.multiply(5, 5)
        self.assertEqual(result, 25)
    
    def test_division(self):
        calc = Calculator()
        result = calc.divide(10, 5)
        self.assertEqual(result, 2)

if __name__ == "__main__":
    unittest.main()
    