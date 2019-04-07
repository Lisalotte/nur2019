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
	for k in range(kaas):
		P.append((mean**k*np.exp(-1.*mean))/np.math.factorial(k))
	return P

# Plotting Poisson distributions
# Values: (1,0), (5,10), (3,20), (2.6,40) (mean, k)
means = [1.,5.,3.,2.6]
kaas = [0,10,20,40]

for a in range(len(means)):
	plt.plot(poissonDis(means[a],kaas[a]))

plt.show()

# 1b. Random Number Generator that returns a random floating-point number between 0 and 1.

# Use a combination of an (M)LCG and a 64-bit XOR-shift
# (M)LCG Multiplicative Linear Congruential Generator
def MLCG(m, n):


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
