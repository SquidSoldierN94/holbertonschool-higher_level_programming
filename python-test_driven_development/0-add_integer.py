#!/usr/bin/python3
def add_integer(a, b=98):
    """
    Add two integers or floats, casting them to integers if necessary.

    Args:
    a: The first number, must be an integer or float.
    b: The second number, must be an integer or float (default is 98).

    Returns:
    The integer addition of a and b.

    Raises:
    TypeError: If a or b are not integers or floats.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if isinstance(a, float):
        a = int(a)
    
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    if isinstance(b, float):
        b = int(b)
    
    return a + b
