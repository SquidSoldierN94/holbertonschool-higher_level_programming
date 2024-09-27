#!/usr/bin/python3
from abc import ABC, abstractmethod
import math

class Shape(ABC):
    
    @abstractmethod
    def area(self):
        """Abstract method that must be implemented by any subclass.
        
        This method is intended to return the area of the shape.
        """
        pass
    
    @abstractmethod
    def perimeter(self):
        """Abstract method that must be implemented by any subclass.
        
        This method is intended to return the perimeter of the shape.
        """
        pass

class Circle(Shape):
    
    def __init__(self, radius):
        """Initialize a Circle instance with a given radius."""
        self.radius = radius
    
    def area(self):
        """Calculate and return the area of the circle.
        
        Formula: π * radius^2
        """
        return math.pi * self.radius ** 2
    
    def perimeter(self):
        """Calculate and return the perimeter of the circle.
        
        Formula: 2 * π * radius
        """
        return 2 * math.pi * self.radius

class Rectangle(Shape):
    
    def __init__(self, width, height):
        """Initialize a Rectangle instance with a given width and height."""
        self.width = width
        self.height = height
    
    def area(self):
        """Calculate and return the area of the rectangle.
        
        Formula: width * height
        """
        return self.width * self.height
    
    def perimeter(self):
        """Calculate and return the perimeter of the rectangle.
        
        Formula: 2 * (width + height)
        """
        return 2 * (self.width + self.height)

def shape_info(shape):
    """Print the area and perimeter of the provided shape."""
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")
