#!/usr/bin/python3
"""
This module provides a function to print a text with 2 new lines after each of the characters: ., ? and :
"""

def text_indentation(text):
    """
    Prints a text with 2 new lines after each of the characters: ., ? and :

    Args:
        text (str): The input text.

    Raises:
        TypeError: If text is not a string.

    Returns:
        None
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    
    punctuation = ['.', '?', ':']
    for char in text:
        print(char, end='')
        if char in punctuation:
            print('\n\n', end='')
