#!/usr/bin/python3
"""This module contains the test cases for the Rectangle class"""
import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """This class tests the Rectangle class"""

    def test_init(self):
        """testting the init method"""
        Rectangle(3, 4, 2, 4, 1)
        self.assertEqual(Rectangle.width(), 3)
        self.assertEqual(Rectangle.height(), 4)
        self.assertEqual(Rectangle.x(), 2)
        self.assertEqual(Rectangle.y(), 4)

    def test_width(self):
        """if the width is an integer"""
        width(3)
        self.assertEqual(width(), 3)

    def test_width_negative(self):
        """what if width is less than zero"""
        with self.assertRaises(ValueError):
            width(-4)
