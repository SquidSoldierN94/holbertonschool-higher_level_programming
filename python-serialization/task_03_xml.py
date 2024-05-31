#!/usr/bin/python3

import xml.etree.ElementTree as ET

def serialize_to_xml(dictionary, filename):
    """
    Serializes a Python dictionary into XML and saves it to a file.

    Parameters:
        dictionary (dict): The dictionary to serialize.
        filename (str): The name of the file to save the XML data to.

    Returns:
        None
    """
    root = ET.Element("data")

    for key, value in dictionary.items():
        element = ET.SubElement(root, key)
        element.text = str(value)

    tree = ET.ElementTree(root)
    tree.write(filename, encoding='utf-8', xml_declaration=True)

def deserialize_from_xml(filename):
    """
    Deserializes XML data from a file into a Python dictionary.

    Parameters:
        filename (str): The name of the file containing the XML data.

    Returns:
        dict: The deserialized dictionary.
    """
    tree = ET.parse(filename)
    root = tree.getroot()

    result = {}
    for element in root:
        result[element.tag] = element.text

    return result
