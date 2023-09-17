#!/usr/bin/python3
"""Check if an object is exactly at instance"""
def is_same_class(obj, a_class):
	"""
	Returns true if the the object is exactly
	an instance of the specified class
	"""
	if type(obj) == a_class:
		return True
	return False
