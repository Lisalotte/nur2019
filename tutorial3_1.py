'''
' Author: Lisa Pothoven
' Student nr: 1328263
' Date: 26 Feb 2019
'
' Tutorial 3.1 Integration of Functions
'''

from matplotlib import pyplot as plt
import numpy as np
from scipy.integrate import quad

def f(x):
	return x**2

# Simple trapezoid rule
def trapezoid(h,lowerlim,upperlim):
	if (h[upperlim] - h[lowerlim] > 0):
		return (h[upperlim]-h[lowerlim])*0.5*f(lowerlim) + trapezoid(lowerlim+1,upperlim-1) + 0.5*f(upperlim)
	return 0.5*(f(lowerlim) + 0.5*f(upperlim))

# Simpson's rule
def simpson(lowerlim, upperlim, h):
	if (upperlim - lowerlim > 2):
		return h/3.*(f(lowerlim)+4.*simpson(lowerlim+1,upperlim-1,((h*2.)-2)*0.5)+f(upperlim))
	elif (upperlim - lowerlim > 1):	
		return h/3.*(f(lowerlim)+4.*f(lowerlim+1)+f(upperlim))
	return 0
'''
def simpson(lowerlim, upperlim, h):
	if (upperlim - lowerlim > 2):
		return h/3.*(f(lowerlim)+4.*simpson(lowerlim+1,upperlim-1,((h*2.)-2)*0.5)+f(upperlim))
	elif (upperlim - lowerlim > 1):	
		return h/3.*(f(lowerlim)+4.*f(lowerlim+1)+f(upperlim))
	return 0
'''	

def main():
	#stepsize
	h = np.linspace(1,5,100)
	print(h)

	print("Trapezoid:", trapezoid(h,0,-1))

	print("Simpson:", simpson(h))

	print("Scipy approximation:", quad(f,1,5)[0])

main()
	
