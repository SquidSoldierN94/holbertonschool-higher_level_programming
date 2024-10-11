#!/usr/bin/python3

import json

def load_from_json_file(filename):
    """
    Loads a Python object from a JSON file.

    Args:
        filename (str): The name of the file containing the JSON data.

    Returns:
        any: The Python object represented by the JSON data in the file.
    """
    with open(filename, 'r') as file:
        return json.load(file)
