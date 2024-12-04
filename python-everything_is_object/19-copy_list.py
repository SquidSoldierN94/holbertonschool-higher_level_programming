#!/usr/bin/env python3

def copy_list(a_list):
    """
    Returns a copy of the given list.

    This function takes a list as input and returns a new list that is a copy
    of the input list. The copy is created using list slicing, which ensures
    that a new list object is created with the same elements as the original.

    Parameters:
    a_list (list): The list to be copied.

    Returns:
    list: A new list that is a copy of the input list.
    """
    return a_list[:]
