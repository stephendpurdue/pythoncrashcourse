import unittest
from problem_set import cities

class TestCities(unittest.TestCase):

    def test_city_country(self):
        formatted_string = cities('santiago', 'chile', str(500000))
        self.assertEqual(formatted_string, 'Santiago, Chile, 500000')

if __name__ == "__main__":
    unittest.main()
