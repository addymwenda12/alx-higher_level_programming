#!/usr/bin/python3
"""class Rectangle that inherits from BaseGeometry"""

class Rectangle(BaseGeometry):
    def __init__(self, width, height):
        self.__width = 0  # Initialize width to 0
        self.__height = 0  # Initialize height to 0
        self.integer_validator("width", width)  # Validate and set width
        self.integer_validator("height", height)  # Validate and set height
        self.__width = width  # Set the width
        self.__height = height  # Set the height

    def area(self):
        """Compute the area of the rectangle."""
        return self.__width * self.__height

    def __str__(self):
        """Return the string representation of the rectangle."""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
