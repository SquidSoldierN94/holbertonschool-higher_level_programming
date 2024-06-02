#!/usr/bin/python3
import json
def from_json_string(my_str):
    """
    Returns a Python object (data structure) represented by a JSON string.

    Parameters:
    my_str (str): The JSON string to deserialize.

    Returns:
    object: The Python object represented by the JSON string.
    """
    from_json = json.loads(my_str)
    return from_json
