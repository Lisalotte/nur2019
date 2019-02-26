'''
' Author: Lisa Pothoven
' Student nr: 1328263
' Date: 19 Feb 2019
'
' Tutorial 2
'''

from matplotlib import pyplot as plt
import numpy as np

'''
' Gaussian Elimination with backsubstitution
'''

def GaussianElimination(matrix,c,r):
	for j in range(0,c): #columns
		for i in range(j+1,r): #rows
			# calculate multiplier (to subract multiplier * a_jj from row i)
			multiplier = matrix[i][j]/matrix[j][j]
			for k in range(j,c): #columns
				# for every element in row i, subtract multiplier * a_jk
				matrix[i][k] = matrix[i][k] - multiplier*matrix[j][k]
	return matrix

def GaussJordanElimination(matrix,c,r):
	for j in range(0,c): #columns
		for i in range(0,r): #rows	
			if ((i != j) and (j < 5)):
				if (matrix[i][j] != 0):	
					matrix[i] = matrix[j][j]*matrix[i] - matrix[i][j]*matrix[j]
	return matrix

def solveMatrix(matrix,c,r,x,y_array):
	my_value = matrix[r][c]
	y = 0
	if (c < 4 and r < 4):
		y += matrix[r][c+1] * solveMatrix(matrix,c+1,r+1,y,y_array)
	if(my_value != 0):
		y = matrix[r][-1]/my_value
	y_array.append(y)
	print(y)
	return x


def main():
	matrix = np.array([
		[3, 8, 1, -12, -4, 2],
		[1, 0, 0, -1, 0, 0],
		[4, 4, 3, -40, -3, 1],
		[0, 2, 1, -3, -2, 0],
		[0, 1, 0, -12, -0, 0]
	],np.float)

	c = 6
	r = 5

	matrix_Gauss = matrix.copy()
	GaussianElimination(matrix_Gauss,c,r)

	matrix_Jordan = matrix.copy()
	GaussJordanElimination(matrix_Jordan,c,r)

	print(matrix)
	print(matrix_Gauss)
	print(matrix_Jordan)
#		print(GaussJordanElimination(matrix_Jordan,c,r))
	x = 0
	y_array = []
	solveMatrix(matrix_Gauss,0,0,x,y_array)
	print(y_array)
#	y_array = []
#	solveMatrix(matrix_Jordan,0,0,x,y_array)
#	print(y_array)

	c = 0
	val = 0
	for y in y_array:
		val += y*matrix[0][c]
		c += 1
	print(val)

main()
				
