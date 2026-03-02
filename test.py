  # test.py

import unittest
from cal import add, subtract, multiply, divide

class TestCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(10, 20), 30)

    def test_subtract(self):
        self.assertEqual(subtract(50, 30), 20)

    def test_multiply(self):
        self.assertEqual(multiply(5, 6), 30)

    def test_divide(self):
        self.assertEqual(divide(20, 5), 4)

    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            divide(10, 0)
-z
if __name__ == "__main__":
    unittest.main()            