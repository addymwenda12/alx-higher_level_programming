#!/usr/bin/python3
"""Checks if an object is an instance of a class that inherited"""


def inherits_from(obj, a_class):
	"""Defines an inherited class-checking function."""
	if issubclass(type(obj), a_class) and type(obj) != a_class:
		return True
	return False
