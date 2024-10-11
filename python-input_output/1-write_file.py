#!/usr/bin/python3

def write_file(filename="", text=""):
    """
    Writes a string to a text file (UTF-8) and returns the number of characters written.

    Args:
        filename (str): The name of the file to write to. Defaults to an empty string, which should be replaced with the actual file name.
        text (str): The string to write to the file. Defaults to an empty string.

    Returns:
        int: The number of characters written to the file.
    """
    with open(filename, 'w', encoding='utf-8') as file:
        num_chars = file.write(text)
    return num_chars
