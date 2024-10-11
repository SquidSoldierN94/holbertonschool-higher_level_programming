#!/usr/bin/python3

def read_file(filename=""):
    """
    Reads a text file and prints its content to stdout.

    Args:
        filename (str): The name of the file to read. Defaults to an empty string, which should be replaced with the actual file name.
    """
    with open(filename, 'r', encoding='utf-8') as file:
        content = file.read()
        print(content)
