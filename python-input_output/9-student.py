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

    def to_dict(self):
        """
        Returns a dictionary representation of the student.

        Returns:
            dict: A dictionary containing the student's attributes.
        """
        return {
            'first_name': self.first_name,
            'last_name': self.last_name,
            'age': self.age
        }
