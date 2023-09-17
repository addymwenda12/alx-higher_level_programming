#!/usr/bin/python3
"""Checks if the object is an instance of a class"""


def is_kind_of_class(obj, a_class):
	"""Defines a class and inherited class-checking function."""
	if isinstance(obj, a_class):
		return True
	return False
