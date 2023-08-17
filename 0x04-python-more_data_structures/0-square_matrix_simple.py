#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
	"""Computes square value of integers"""
	squared_matrix = []
	for row in matrix:
		#square each element using map
		squared_row = list(map(lambda x: x ** 2, row))
		# Add the squared row to the squared matrix
		squared_matrix.append(squared_row)
	return (squared_matrix)
