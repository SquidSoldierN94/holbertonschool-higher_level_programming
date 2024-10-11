#!/usr/bin/python3

import json

def to_json_string(my_obj):
    """
    Converts a Python object to a JSON string.

    Args:
        my_obj (any): The Python object to be converted to a JSON string. This can be any serializable Python object.

    Returns:
        str: The JSON string representation of the Python object.
    """
    return json.dumps(my_obj)
