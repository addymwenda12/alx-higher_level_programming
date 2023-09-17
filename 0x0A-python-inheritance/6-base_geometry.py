#!/usr/bin/python3
"""Public instance method that raise Exception"""


class BaseGeometry:
	"""Raising an Excption message"""
	def area(self):
		raise Exception("area() is not implemented")
