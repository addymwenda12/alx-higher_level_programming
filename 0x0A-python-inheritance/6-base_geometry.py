#!/usr/bin/python3
"""Public instance method that raise Exception"""


class BaseGeometry:
	def area(self):
		raise Exception("area() is not implemented")
