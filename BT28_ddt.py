import sys
from setuptools import setup
# sys.path.append(r"")

import unittest
from ddt import ddt,unpack,data
from MyMathModule import is_prime, plus,divide



@ddt
class DDTSample(unittest.TestCase):
    def setUp(self) -> None:
        print("My Setup")
    
    def tearDown(self) -> None:
        print("My Teardown")

    @data(3,5,7,9,10)
    def test_is_prime(self,value):
        print(value)
        self.assertTrue(is_prime(value))

    @data([1,2,3],[2,3,5],[5,6,11])
    @unpack
    def test_plus(self,value1,value2,value3):
        self.assertEqual(plus(value1,value2),value3)

    @data([9,3,3],[5,5,1],[7,8,9])
    @unpack
    def test_divide(self,value1,value2,value3):
        self.assertEqual(divide(value1,value2),value3)

if __name__ == '__main__':
    unittest.main()
    