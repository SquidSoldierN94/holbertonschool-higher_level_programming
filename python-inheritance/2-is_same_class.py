#!/usr/bin/python3

def is_same_class(obj, a_class):
    """
    Check if obj is exactly an instance of a_class.
    
    Args:
        obj: The object to check.
        a_class: The class to check against.
    
    Returns:
        True if obj is exactly an instance of a_class, otherwise False.
    """
    return type(obj) is a_class
