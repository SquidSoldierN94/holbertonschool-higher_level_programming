#!/usr/bin/python3

def append_write(filename="", text=""):
    """
    Appends a string to the end of a text file (UTF-8) and returns the number of characters written.

    Args:
        filename (str): The name of the file to append to. Defaults to an empty string, which should be replaced with the actual file name.
        text (str): The string to append to the file. Defaults to an empty string.

    Returns:
        int: The number of characters appended to the file.
    """
    with open(filename, 'a', encoding='utf-8') as file:
        num_chars = file.write(text)
    return num_chars
