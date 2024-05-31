#!/usr/bin/python3
import json

def serialize_and_save_to_file(data, filename):
    """
    Serialize a dictionary and save it to a JSON file.

    Parameters:
        data (dict): The dictionary to serialize.
        filename (str): The name of the file to save the JSON data to.

    Returns:
        None
    """
    with open(filename, 'w') as file:
        json.dump(data, file)

def load_and_deserialize(filename):
    """
    Load JSON data from a file and deserialize it into a dictionary.

    Parameters:
        filename (str): The name of the file to read the JSON data from.

    Returns:
        dict: The deserialized dictionary.
    """
    with open(filename, 'r') as file:
        data = json.load(file)
    return data
