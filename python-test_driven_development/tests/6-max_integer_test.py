#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """Test cases for the max_integer function"""

    def test_normal_case(self):
        """Test with a list of multiple positive integers"""
        result = max_integer([1, 2, 3, 4])
        self.assertEqual(result, 4)

    def test_mixed_case(self):
        """Test with a list of positive and negative integers"""
        result = max_integer([1, -2, 3, -4])
        self.assertEqual(result, 3)

    def test_single_element(self):
        """Test with a list containing a single element"""
        result = max_integer([7])
        self.assertEqual(result, 7)

    def test_empty_list(self):
        """Test with an empty list"""
        result = max_integer([])
        self.assertIsNone(result)

    def test_repeated_elements(self):
        """Test with a list containing repeated maximum elements"""
        result = max_integer([5, 5, 5, 5])
        self.assertEqual(result, 5)

    def test_floats(self):
        """Test with a list containing float values"""
        result = max_integer([1.5, 2.5, 0.5, 3.5])
        self.assertEqual(result, 3.5)

    def test_negative_integers(self):
        """Test with a list containing only negative integers"""
        result = max_integer([-1, -2, -3, -4])
        self.assertEqual(result, -1)

if __name__ == '__main__':
    unittest.main()