'''
' Author: Lisa Pothoven
' Student nr: 1328263
' Date: 19 Feb 2019
'
' Tutorial 2
'''

from matplotlib import pyplot as plt
import numpy as np

def GaussianElimination(matrix,c,r):
	'''
	Gaussian Elimination
	'''
	for j in range(0,c): #columns
		for i in range(j+1,r): #rows
			# calculate multiplier (to subract multiplier * a_jj from row i)
			multiplier = matrix[i][j]/matrix[j][j]
			for k in range(0,c): #columns
				# for every element in row i, subtract multiplier * a_jk
				matrix[i][k] = matrix[i][k] - multiplier*matrix[j][k]
	return matrix

def GaussJordanElimination(matrix,c,r):
	'''
	Gauss-Jordan elimination
	'''
	for j in range(0,c): #columns
		for i in range(0,r): #rows	
			if ((i != j) and (j < 5)):
				if (matrix[i][j] != 0):	
					matrix[i] = matrix[j][j]*matrix[i] - matrix[i][j]*matrix[j]
	return matrix

def backSubstitution(matrix,c,r,x,x_array):
	'''
	Back-substitution
	'''
	if(c < matrix.shape[1] and r < matrix.shape[0]):
		x = 1./matrix[r][c] * (matrix[r][-1] - matrix[r][c+1] * solveMatrix(matrix,c+1,r+1,x,x_array))
		x_array.append(x)
	return x

#TODO: LU-decomposition method using scipy libraries
#TODO: Compare computation times for each method

def main():
	matrix = np.array([
		[3, 8, 1, -12, -4, 2],
		[1, 0, 0, -1, 0, 0],
		[4, 4, 3, -40, -3, 1],
		[0, 2, 1, -3, -2, 0],
		[0, 1, 0, -12, -0, 0]
	],np.float)

	c = 6 #columns
	r = 5 #rows

	matrix_Gauss = matrix.copy()
	GaussianElimination(matrix_Gauss,c,r)

	matrix_Jordan = matrix.copy()
	GaussJordanElimination(matrix_Jordan,c,r)
	
	print(matrix_Gauss)
	print(matrix_Jordan)

	# Solve Gaussian elimination matrix
	y_array = []
	backSubstitution(matrix_Gauss,0,0,0,y_array)
	print(y_array)

	# Solve Jordan elimination matrix
	y_array = []
	backSubstitution(matrix_Jordan,0,0,0,y_array)
	print(y_array)

	# Check with numpy
	y_array = np.linalg.solve(matrix[:,:-1],matrix[:,-1])
	print(y_array)


main()
				
