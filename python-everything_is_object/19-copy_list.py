#!/usr/bin/python3

"""
This module defines a function `copy_list` that creates a copy of a given list.

The opy of the input list, meaning that the original
list remains unchanged, and any modifications to the new list will not affect
the original one.

The function can handle lists containing any type of objects.

No external modules are required for this implementation.

Function:
    - copy_list(a_list: List[Any]) -> List[Any]:
        Returns a new list containing the same elements as the input list.

Parameters:
    a_list (List[Any]): The input list to be copied.

Returns:
    List[Any]: A new list containing the same elements as the input list.
"""


def copy_list(a_list):
    return a_list[:]
