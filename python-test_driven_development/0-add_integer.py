#!/usr/bin/python3
"""
This module provides a function to add two integers.
"""

def add_integer(a, b=98):
    """
    Adds two integers or floats, casting them to integers if necessary.

    Args:
        a (int/float): The first number.
        b (int/float): The second number, default is 98.

    Raises:
        TypeError: If a or b are not integers or floats.

    Returns:
        int: The sum of a and b.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    
    return int(a) + int(b)
