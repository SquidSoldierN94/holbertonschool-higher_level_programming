#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
from 6-max_integer import max_integer

class TestMaxInteger(unittest.TestCase):
    """Test cases for the max_integer function."""

    def test_regular_list(self):
        """Test with a normal list of integers."""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_single_element(self):
        """Test with a list containing a single integer."""
        self.assertEqual(max_integer([5]), 5)

    def test_negative_numbers(self):
        """Test with a list containing negative integers."""
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)
        self.assertEqual(max_integer([-10, -20, -30]), -10)

    def test_mixed_numbers(self):
        """Test with a list containing both positive and negative integers."""
        self.assertEqual(max_integer([-1, 0, 1]), 1)
        self.assertEqual(max_integer([0, -1, 1]), 1)

    def test_empty_list(self):
        """Test with an empty list."""
        self.assertIsNone(max_integer([]))

    def test_identical_elements(self):
        """Test with a list where all elements are the same."""
        self.assertEqual(max_integer([2, 2, 2, 2]), 2)

    def test_large_numbers(self):
        """Test with a list containing very large integers."""
        self.assertEqual(max_integer([1000000000, 1000000001, 1000000002]), 1000000002)

    def test_floats(self):
        """Test with a list containing floats, which should be converted to integers."""
        self.assertEqual(max_integer([1.0, 2.1, 3.5]), 3)

    def test_string_elements(self):
        """Test with a list containing strings (should raise TypeError)."""
        with self.assertRaises(TypeError):
            max_integer(["a", "b", "c"])

if __name__ == '__main__':
    unittest.main()
