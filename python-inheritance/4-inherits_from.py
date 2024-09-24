#!/usr/bin/python3

def inherits_from(obj, a_class):
    """
    Check if obj is an instance of a class that inherited (directly or indirectly)
    from the specified class, but not an instance of the specified class itself.
    
    Args:
        obj: The object to check.
        a_class: The class to check against.
    
    Returns:
        True if obj is an instance of a class that inherited from a_class,
        but not an instance of a_class itself, otherwise False.
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
