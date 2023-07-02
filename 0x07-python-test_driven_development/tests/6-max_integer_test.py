#!/usr/bin/python3
"""This module is the test case for the max integer function"""


import unittest
max_integer = __import__('6-max_integer').max_integer


class MaxIntegerTestCase(unittest.TestCase):
    """Test modules go here"""

    def testForOrderedIntegers(self):
        """Checks whether the function would work for an ordered list"""
        order = [2, 4, 6, 8]
        self.assertEqual(max_integer(order), 8)

    def testForUnorderedIntegers(self):
        """Checks whetehr the function will work fr an unordered list"""
        unorder = [3, 9, 12, 6, 5, 4]
        self.assertEqual(max_integer(unorder), 12)

    def testWithUnorderedFloats(self):
        """Checks whether the function will work for floats"""
        unorder = [5.0, 6.2, 3.33, 2.090, 10.34]
        self.assertEqual(max_integer(unorder), 10.34)

    def testWithOrderedFloats(self):
        """Checks whether the function works with ordered floats"""
        order = [1.0, 2.0, 3.0, 4.0]
        self.assertEqual(max_integer(order), 4.0)

    def testEmptyList(self):
        """Checks whether the function will work with an empty list"""
        empty = []
        self.assertEqual(max_integer(empty), None)

    def testMixture(self):
        """Checks whether it works if it's a mixture of ints and floats"""
        mixture = [1, 5, 6.4, -3, 0.5555, 22]
        self.assertEqual(max_integer(mixture), 22)


if __name__ == '__main__':
    unittest.main()
