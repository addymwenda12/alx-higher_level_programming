#!/usr/bin/python3
"""class Square that inherits from Rectangle"""

class Square(Rectangle):
	"""implementation of Rectangle"""
	def __init__(self, size):
		self.__size = 0
		self.integer_validator("size", size)
		self.__size = size
		super().__init__(size, size)

	def __str__(self):
		return "[Square] {}/{}".format(self.__size, self.__size)
