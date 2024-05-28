#!/usr/bin/python3
class MyClass:
    def __init__(self, first_name, last_name, age):
        """
        Initializes a MyClass instance with the provided attributes.

        Parameters:
            first_name (str): The first name of the person.
            last_name (str): The last name of the person.
            age (int): The age of the person.

        Returns:
            None
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_dict(self):
        """
        Returns a dictionary representation of the object.

        Returns:
            dict: A dictionary containing the object's attributes.
        """
        return {
            'first_name': self.first_name,
            'last_name': self.last_name,
            'age': self.age
        }
