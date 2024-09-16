
import unittest
import logics


class TestCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(logics.add(5, 10), 15)
        self.assertEqual(logics.add(-5, 10), 5)
        self.assertEqual(logics.add(-5, -10), -15)
        self.assertEqual(logics.add(0, -10), 10)
        self.assertEqual(logics.add(0, 10), 10)
        self.assertEqual(logics.add(0, 0), 0)


    def test_divide(self):
        self.assertEqual(logics.divide(5, 10), 0.5)
        self.assertEqual(logics.divide(-5, 10), 0.5)

        with self.assertRaises(ValueError) as context:
            logics.divide(10, 0)

        self.assertEqual(str(context.exception), "Cannot divide by zero")




if __name__ == '__main__':
    unittest.main()