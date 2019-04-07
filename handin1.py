'''
' Author: Lisa Pothoven
' Student nr: 1328263
' Date: March 2019
'
' Hand-in ex. 1
'''

import numpy as np
from matplotlib import pyplot as plt

# 1a. Poisson probability distribution
def poissonDis(mean, kaas):
	if (mean == 0):
		print("Error. Mean is 0")
		return 0
	k = 0	
	P = []
	for k in range(kaas+1):
		P.append((mean**k*np.exp(-1.*mean))/np.math.factorial(k)) #TODO change this self-written routine
	return P

# Plotting Poisson distributions
# Values: (1,0), (5,10), (3,20), (2.6,40) (mean, k)
means = np.array([1.,5.,3.,2.6], np.float64) #TODO: bonus
kaas = np.array([0,10,20,40], np.int64)

for a in range(len(means)):
	poissonResult = poissonDis(means[a],kaas[a])
	plt.plot(poissonResult)
	print(means[a],kaas[a], ": %.5e" %poissonResult[kaas[a]-1])

plt.show()

# 1b. Random Number Generator that returns a random floating-point number between 0 and 1.

# Use a combination of an (M)LCG and a 64-bit XOR-shift
# (M)LCG Multiplicative Linear Congruential Generator
def MLCG(x, a, m):
	# x should start as 1<=x<=m-1 or low 32-bits
	return a * x % m

# XOR-shift
def XORshift(x):
	# Start with a 64-bit x != 0
	# TODO values?
	a1 = 21
	a2 = 35
	a3 = 4	

	x = x ^ (x >> a1)
	x = x ^ (x << a2)
	x = x ^ (x >> a3)

	return x



# Test: plot sequential random numbers against each other in a scatter plot for the first 1000 numbers.

# Test: generate 1,000,000 numbers and plot in 20 bins of 0.05 wide.

# Fixed seed (= first output value)



