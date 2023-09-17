#!/usr/bin/python3
"""Inherits from list"""
class MyList(list):
	"""Prints lists in ascending order"""
	def print_sorted(self):
		sorted_list = sorted(self)
		print(sorted_list)
