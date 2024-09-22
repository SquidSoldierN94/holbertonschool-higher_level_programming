#!/usr/bin/python3
"""
This module provides a function to print text with 2 new lines after each
of these characters: ., ? and :.
"""

def text_indentation(text):
    """
    Prints text with 2 new lines after each of these characters: ., ?, and :.

    Args:
        text (str): The text to be printed.

    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    special_chars = {'.', '?', ':'}
    result = ""
    i = 0

    while i < len(text):
        result += text[i]
        if text[i] in special_chars:
            result += "\n\n"
            i += 1
            while i < len(text) and text[i] == ' ':
                i += 1
            continue
        i += 1

    print(result, end="")
