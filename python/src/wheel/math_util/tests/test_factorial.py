import unittest
from math_util.factorial import factorial


class TestFactorial(unittest.TestCase):
    """
    to run test use 

    python3 -m unittest discover -s tests/

    """

    def test_factorial_zero(self):
        self.assertEqual(factorial(0), 1)

    def test_factorial_one(self):
        self.assertEqual(factorial(0), 1)

    def test_factorial_positive(self):
        self.assertEqual(factorial(2), 2)
        self.assertEqual(factorial(3), 6)
        self.assertEqual(factorial(4), 24)
    
    def test_factorial_negative(self):
        with self.assertRaises(ValueError): factorial(-1)
    
