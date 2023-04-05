import unittest

from pip import main
from MyMathModule import is_prime
from MyMathModule import plus
from MyMathModule import divide

class testcaseSample(unittest.TestCase):
    def test_prime(self):
        self.assertFalse(is_prime(10))

    def test_prime1(self):
        self.assertFalse(is_prime(5))
    
    def test_plus(self):
        self.assertEqual(plus(2,5),7)
    
    def test_divide(self):
        self.assertEqual(divide(4,4),1)

if __name__ == '__main__':
    unittest.main()
    