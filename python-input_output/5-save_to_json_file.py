#!/usr/bin/python3

import json

def save_to_json_file(my_obj, filename):
    """
    Saves a Python object to a file in JSON format.

    Args:
        my_obj (any): The Python object to be saved to the file. This can be any serializable Python object.
        filename (str): The name of the file to save the JSON data.

    Returns:
        None
    """
    with open(filename, 'w') as file:
        json.dump(my_obj, file)
