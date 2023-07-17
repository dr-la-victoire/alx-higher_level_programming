#!/usr/bin/python3
"""This module has the test cases for the base class"""
import unittest
from models.base import Base


class BaseTest(unittest.TestCase):
    """This class is the test class for the base class"""

    def test_id(self):
        """Testing the id field"""
        base_id = Base(20)
        self.assertEqual(20, base_id.id)

    def test_no_id(self):
        """With no id inputed"""
        base_id = Base()
        self.assertEqual(1, base_id.id)

    def test_id_is_a_string(self):
        """If ID is a string"""
        base_id = Base("String")
        self.assertEqual("String", base_id.id)

    def test_id_less_than_zero(self):
        """If ID is less than zero"""
        basse_id = Base(-59)
        self.assertEqual(-59, basse_id.id)

    def test_if_id_is_a_lilst(self):
        """what if id is a list"""
        bases_id = Base([1, 2, 4, "indigo"])
        self.assertEqual([1, 2, 4, "indigo"], bases_id.id)

    # def test_to_json_string(self):
        """This method tests the t0_json_string method"""

