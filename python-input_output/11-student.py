#!/usr/bin/python3
class Student:
    def __init__(self, first_name, last_name, age):
        """
        Initializes a Student instance with the provided attributes.

        Parameters:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.

        Returns:
            None
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Returns a dictionary representation of the student.

        Parameters:
            attrs (list of str, optional): List of attributes to include in the dictionary representation.
                                           If not provided, all attributes are included.

        Returns:
            dict: A dictionary containing the student's attributes.
        """
        if attrs is None:
            attrs = ['first_name', 'last_name', 'age']

        return {attr: getattr(self, attr) for attr in attrs if hasattr(self, attr)}
