import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):

    def setUp(self):
        print("setUp Method")
        self.employee1 = Employee('John', 'Doe', 2000)
        self.employee2 = Employee('Jane', 'Doe', 3000)

    def tearDown(self):
        print("tearDown Method")

    def test_fullname(self):
        print("test_fullname Method")

        self.assertEqual(self.employee1.fullname, 'John Doe')
        self.assertEqual(self.employee2.fullname, 'Jane Doe')

        self.employee1.first_name = 'Bob'
        self.employee2.first_name = 'Kate'

        self.assertEqual(self.employee1.fullname, 'Bob Doe')
        self.assertEqual(self.employee2.fullname, 'Kate Doe')

    def test_applyraises(self):
        print("test_applyraises Method")

        self.employee1.apply_raise()
        self.employee2.apply_raise()

        self.assertEqual(self.employee1.salary, 4000)
        self.assertEqual(self.employee2.salary, 6000)
