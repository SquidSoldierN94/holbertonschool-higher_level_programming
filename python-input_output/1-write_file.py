#!/usr/bin/python3
def write_file(filename="", text=""):
    """
    Writes a string to a text file (UTF8) and returns the number of characters written.

    Parameters:
    filename (str): The name of the file to write to. Defaults to an empty string.
    text (str): The string to write to the file. Defaults to an empty string.

    Returns:
    int: The number of characters written to the file.
    """
    with open(filename, 'w', encoding='utf-8') as file:
        content = file.write(text)
    return content
