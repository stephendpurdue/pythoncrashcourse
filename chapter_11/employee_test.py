from problem_set import Employee
import unittest

class TestEmployee(unittest.TestCase):
    
    def setUp(self):
        self.employee_information = Employee('Stephen', 'Purdue', 30000)

    def test_give_default_raise(self):
        self.employee_information.give_default_raise()
        self.assertEqual(self.employee_information.annual_salary, 35000)

    def test_give_custom_raise(self):
        self.employee_information.give_custom_raise(10000)
        self.assertEqual(self.employee_information.annual_salary, 40000)

if __name__ == '__main__':
    unittest.main()