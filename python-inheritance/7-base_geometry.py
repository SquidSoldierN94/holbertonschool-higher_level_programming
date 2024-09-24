#!/usr/bin/python3

class BaseGeometry:
    """
    A class representing basic geometry.

    This class provides an interface for geometric shapes.
    It includes methods to calculate the area and validate integer values.
    """

    def area(self):
        """
        Calculate the area of the geometric shape.

        Raises:
            Exception: area() is not implemented.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validate the value as a positive integer.

        Args:
            name (str): The name of the variable being validated.
            value (int): The value to validate.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
