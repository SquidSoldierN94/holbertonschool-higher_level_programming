#!/usr/bin/python3
class Rectangle:
    """
    A class to represent a rectangle.
    
    Attributes:
    -----------
    width : int
        The width of the rectangle (default is 0).
    height : int
        The height of the rectangle (default is 0).
    """
    
    def __init__(self, width: int = 0, height: int = 0):
        """
        Initializes a new Rectangle instance.
        
        Parameters:
        -----------
        width : int, optional
            The width of the rectangle (default is 0).
        height : int, optional
            The height of the rectangle (default is 0).
        """
        self.width = width
        self.height = height

    @property
    def width(self) -> int:
        """
        Gets the width of the rectangle.
        
        Returns:
        --------
        int
            The width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value: int) -> None:
        """
        Sets the width of the rectangle.
        
        Parameters:
        -----------
        value : int
            The new width of the rectangle.
        
        Raises:
        -------
        TypeError:
            If the value is not an integer.
        ValueError:
            If the value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self) -> int:
        """
        Gets the height of the rectangle.
        
        Returns:
        --------
        int
            The height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value: int) -> None:
        """
        Sets the height of the rectangle.
        
        Parameters:
        -----------
        value : int
            The new height of the rectangle.
        
        Raises:
        -------
        TypeError:
            If the value is not an integer.
        ValueError:
            If the value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self) -> int:
        """
        Calculates the area of the rectangle.
        
        Returns:
        --------
        int
            The area of the rectangle.
        """
        return self.__width * self.__height

    def perimeter(self) -> int:
        """
        Calculates the perimeter of the rectangle.
        
        Returns:
        --------
        int
            The perimeter of the rectangle.
            If width or height is 0, the perimeter is 0.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self) -> str:
        """
        Returns a string representation of the rectangle using the `#` character.
        
        Returns:
        --------
        str
            The string representation of the rectangle.
            If width or height is 0, returns an empty string.
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        return "\n".join(["#" * self.__width for _ in range(self.__height)])

    def __repr__(self) -> str:
        """
        Returns a string representation of the rectangle to recreate a new instance.
        
        Returns:
        --------
        str
            The string representation of the rectangle.
        """
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """
        Prints a message when an instance of Rectangle is deleted.
        """
        print("Bye rectangle...")
