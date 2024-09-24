#!/usr/bin/python3

class BaseGeometry:
    """
    A class representing basic geometry.

    This class provides an interface for geometric shapes.
    It includes a method to calculate the area which must
    be implemented by any subclass.
    """

    def area(self):
        """
        Calculate the area of the geometric shape.

        Raises:
            Exception: area() is not implemented.
        """
        raise Exception("area() is not implemented")
