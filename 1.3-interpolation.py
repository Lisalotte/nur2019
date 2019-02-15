#
# Author: Lisa Pothoven
# Student nr: 1328263
# Date: 12 Feb 2019
#

from matplotlib import pyplot as plt
import numpy as np

xx = np.linspace(1,20,7)

def func(x):
	return 2.0*x*np.sin(0.8*x)
	
#plt.plot(xx, func(xx))
#plt.show()

x_interpol = np.linspace(1,25,100)
y_interpol = np.zeros(100)

#
# LINEAR INTERPOLATION
#
# split(i, x_split)
# This function splits the given array in two and finds the half where your interpolation value lies.
# This half if halfed until the two closest values are found.
#
'''
def split(i, x_split):
	half = int(len(x_split)/2)
	if (x_interpol[i] > x_split[half]):
		x_split = x_split[half:]
	else:
		x_split = x_split[:half+1]	
	if (half > 1):
		x_split = split(i, x_split)
	return x_split
'''
def split(i, x_split, x0, x1):
	half = int(len(x_split)/2)
	if (x_interpol[i] > x_split[half]):
		x_split = x_split[half:]
	else:
		x_split = x_split[:half+1]	
	x0 = np.where(xx==x_split[0])
	x1 = np.where(xx==x_split[-1])
	if (half > 1):
		x_split, x0, x1 = split(i, x_split, x0, x1)
	return x_split, x0, x1

def linearInterpol(i, x_split, x0, x1):
	y0 = func(x_split[0])
	if (len(x_split)>1): 
		y1 = func(x_split[1])
		return (x_interpol[i]-x_split[0])*(y1-y0)/(x_split[1]-x_split[0])+y0
	else:	
		return (x_interpol[i]-x_split[0])*(y0-func(xx[x0-1]))/(x_split[0]-xx[x0-1])+y0
'''		
y_interpol = []
x0 = 0
x1 = len(xx)-1
for i in range(len(x_interpol)):
	x_split, x0, x1 = split(i, xx, x0, x1)
	y_interpol.append(linearInterpol(i, x_split, x0[0], x1[0]))
	
#plt.plot(x_interpol, y_interpol)
#plt.show()
'''
#	
# POLYNOMIAL INTERPOLATION	
#
# 
#def neville(x_data, y_data, x_interpol):

# Let P0 be the value of x0, P1 of x1 etc.
# P01 is the polynomial passing through x0,y0 and x1,y1
# 
def polynomial(x, y, M, x_interp):
	poly = 0
	for i in range(0,M-1):
		for j in range(0,M-1):
			if (i != j):
				next *= y[j]*(x_interp-x[j])/(x[i]-x[j]) 
		poly += next
	return poly

def neville(parents, x, x_interp, M, j_counter):
	children = []
	j = j_counter
	for i in range(0,M-1):
		child = ((x_interp - x[j])*parents[i]-(x_interp-x[i])*parents[i+1])/(x[i]-x[j])
		children.append(child)
		j += 1
	if (len(children)>1):
		j_counter += 1
		M -= 1
		child = neville(children, x, x_interp, M, j_counter)
	return child

def push(array, value):
	array.append(0)
	i = len(array)
	while (i>1):
		array[i-1] = array[i-2]
		i -= 1
	array[0] = value
	return array	
		
interpolated = []
for i in range(len(x_interpol)):
	M = int(4)
	x_surrounding = []
	x_below = 0
	x_above = len(xx)-1
	x_split, x_below, x_above = split(i, xx, x_below, x_above)
	x_surrounding.append(xx[x_below[0][0]])
	x_surrounding.append(xx[x_above[0][0]])

	if (x_below[0][0] > 0):
		push(x_surrounding,xx[x_below[0][0]-1])
	else:
		M -= 1
	if (x_above[0][0] < len(xx)-1):
		x_surrounding.append(xx[x_above[0][0]+1])
	else:
		M -=1
	if (x_interpol[i] > xx[-1]):
		x_surrounding = xx[-2:]
		M = 2

	interpolated.append(neville(func(np.array(x_surrounding)), x_surrounding, x_interpol[i], M, 1))

plt.plot(x_interpol,interpolated)
plt.show()
				

	

	  
