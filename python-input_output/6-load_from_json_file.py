#!/usr/bin/python3
import json
def load_from_json_file(filename):
    """
    Creates an object from a JSON file.

    Parameters:
    filename (str): The name of the JSON file to load.

    Returns:
    object: The Python object created from the JSON data in the file.
    """
    with open(filename, 'r') as file:
        loaded_json = json.load(file)
    return loaded_json
