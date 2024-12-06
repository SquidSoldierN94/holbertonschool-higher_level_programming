#!/usr/bin/python3

def copy_list(a_list):
    """
    Creates a shallow copy of the provided list.

    This function takes a list as input and returns a new list that contains the
    same elements. The new list is a shallow copy, meaning that if the original
    list contains mutable objects (e.g., lists, dictionaries), those objects
    are not copied but merely referenced.

    Parameters:
        a_list (list): The list to be copied.

    Returns:
        list: A new list containing the same elements as the input list.
    """
    return [item for item in a_list]
