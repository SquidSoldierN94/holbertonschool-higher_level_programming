#!/usr/bin/python3

"""
This module that creates a shallow copy of a list.
It demonstrates the use of list comprehension for copying a list.
"""


def copy_list(a_list):

    """
    Returns a copy of the given list.

    This function is a copy of the original list
    provided as input. It uses list comprehension to achieve this.

    Parameters:
    a_list (list): The list to be copied.

    Returns:
    list: A new list that contains the same elements as the original list.
    """
    return [item for item in a_list]
