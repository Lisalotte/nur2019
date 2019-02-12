#
# Author: Lisa Pothoven
# Student nr: 1328263
# Date: 12 Feb 2019
#

from matplotlib import pyplot as plt
import numpy as np

xx = np.linspace(1,20,7)

def func(x):
	return 2*x*np.sin(0.8*x)
	
plt.plot(xx, func(xx))
plt.show()

x_interpol = np.linspace(1,25,100)
y_interpol = np.zeros(100)

#
# LINEAR INTERPOLATION
#
# split(i, x_split)
# This function splits the given array in two and finds the half where your interpolation value lies.
# This half if halfed until the two closest values are found.
#
def split(i, x_split):
	half = int(len(x_split)/2)
	if (x_interpol[i] > x_split[half]):
		x_split = x_split[half:]
	else:
		x_split = x_split[:half+1]	
	if (half > 1):
		x_split = split(i, x_split)
	return x_split

def linearInterpol(i, x_split):
	y0 = func(x_split[0])
	if (len(x_split)>1): 
		y1 = func(x_split[1])
		return (x_interpol[i]-x_split[0])*(y1-y0)/(x_split[1]-x_split[0])
	else:	
		return (x_interpol[i]-x_split[0])*(y0/x_split[0])
		
y_interpol = []
for i in range(len(x_interpol)):
	y_interpol.append(linearInterpol(i, split(i, xx)))
	
plt.plot(x_interpol, y_interpol)
plt.show()
	
#	
# POLYNOMIAL INTERPOLATION	
#
# 
