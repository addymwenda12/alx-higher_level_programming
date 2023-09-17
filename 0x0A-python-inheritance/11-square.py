#!/usr/bin/python3
"""class Square that inherits from Rectangle"""

class Square(Rectangle):
    """Implementation of Rectangle"""
    def __init__(self, size):
        self.__size = 0  # Initialize size to 0
        self.integer_validator("size", size)  # Validate and set size
        self.__size = size  # Set the size
        super().__init__(size, size)  # Call the constructor of the base class (Rectangle) with the same size for width and height

    def __str__(self):
        """Return the string representation of the square."""
        return "[Square] {}/{}".format(self.__size, self.__size)
