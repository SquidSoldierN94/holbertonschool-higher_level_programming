#!/usr/bin/python3
import json
def save_to_json_file(my_obj, filename):
    """
    Writes an object to a text file using its JSON representation.

    Parameters:
    my_obj: The object to be serialized to JSON.
    filename (str): The name of the file to save the JSON representation to.

    Returns:
    None
    """
    with open(filename, 'w') as file:
        json.dump(my_obj, file)
