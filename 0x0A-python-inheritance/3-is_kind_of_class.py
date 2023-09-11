#!/usr/bin/python3

def is_kind_of_class(obj, a_class):
	"""Defines a class and inherited class-checking function."""
	if isinstance(obj, a_class):
		return True
	return False
