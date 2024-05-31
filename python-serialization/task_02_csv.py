#!/usr/bin/python3

import csv
import json

def convert_csv_to_json(csv_filename):
    """
    Converts data from a CSV file to JSON format and writes it to a file.

    Parameters:
        csv_filename (str): The name of the CSV file to convert.

    Returns:
        bool: True if conversion is successful, False otherwise.
    """
    try:
        with open(csv_filename, mode='r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            data = [row for row in csv_reader]
            with open('data.json', mode='w') as json_file:
                json.dump(data, json_file, indent=4)
        return True
    except FileNotFoundError:
        return False
