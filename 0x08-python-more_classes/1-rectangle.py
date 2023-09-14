#!/usr/bin/python3
"""Defines a Rectangle class"""

class Rectangle:
	def __init__(self, width=0, height=0):
		self.__width = width
		self.__height = height

	# Property
	def width(self):
		return self.__width
	
	# Width.setter
	def width(self, value):
		if not isinstance(value, int):
			raise TypeError("width must be an integer")
		if value < 0:
			raise ValueError("width must be >= 0")
		self.__width = value

	# Property
	def height(self):
		return self.__height
	
	# Height setter
	def height(self, value):
		if not isinstance(value, int):
			raise TypeError("height must be an integer")
		if value < 0:
			raise ValueError("height must be >=0")
		self.__height = value
