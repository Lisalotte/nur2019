'''
' Author: Lisa Pothoven
' Student nr: 1328263
' Date: March 2019
'
' Hand-in ex. 1
'''

import numpy as np
from matplotlib import pyplot as plt
import sys

'''
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

#plt.show()
'''
# 1b. Random Number Generator that returns a random floating-point number between 0 and 1.

#TODO remove###################################
def intoBinary(number):
    binarynumber=""
    if (number!=0):
        while (number>=1):
            if (number %2==0):
                binarynumber=binarynumber+"0"
                number=number/2
            else:
                binarynumber=binarynumber+"1"
                number=(number-1)/2
     
    else:
        binarynumber="0"
     
    return "".join(reversed(binarynumber))
###############################################
def int2float(value):
# https://stackoverflow.com/questions/20302904/converting-int-to-float-or-float-to-int-using-bitwise-operations-software-float
	# 0 is 0.0
	if (value == 0):
		return 0.0

	if (value == 1 << 31): #-2**31
		return float(-sys.maxsize-1)
	
	sign = np.int32(0)
	if (value < 0):
		sign = -2**31
		value = -value
	print(sign)
	abs_value_copy = value

	bit_num = 31
	shift_count = 0
	print(abs_value_copy, bit_num, (1 << bit_num))
	print(abs_value_copy & (1 << bit_num))
	while (bit_num > 0):
		if (abs_value_copy & (1 << bit_num)):
			print(intoBinary(1<<bit_num))
			if (bit_num >= 23):
				# shift right
				shift_count = bit_num - 23;
				print("A", abs_value_copy, intoBinary(abs_value_copy))
				abs_value_copy = abs_value_copy >> shift_count
				print(abs_value_copy, intoBinary(abs_value_copy))
			else:
				# shift left
				shift_count = 23 - bit_num
				abs_value_copy = abs_value_copy << shift_count
			break
		bit_num -= 1

	exp = bit_num + 127
	coeff = abs_value_copy & ~(1<<23)
	exp <<= 23

	print(intoBinary(sign), intoBinary(exp), intoBinary(coeff))
	rfloat = (sign | exp | coeff)
	print(-1*intoBinary(rfloat))
	return rfloat

# Use a combination of an (M)LCG and a 64-bit XOR-shift
# (M)LCG Multiplicative Linear Congruential Generator
def MLCG(x, a):
	# Start with a 64-bit x!=0
	return a * x % 2**64

# recommended values for a
a = np.int64(4294957665)
#a = np.array([4294963023, 4162943475, 3947008974, 3874257210, 2936881968, 2811536238, 2654432763, 1640531364], np.int64)

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

def findNorm(array):
	minim = 0
	maxim = 0
	for elem in array:
		if (elem < minim):
			minim = elem
		elif (elem > maxim):
			maxim = elem
	if (-1*minim > maxim):
		return -1*minim
	return maxim

# Fixed seed (= first output value)
x = np.int64(7)
x_prev = np.int64(0)
n = 1000
xarray = np.empty(n,np.int64)
xparray = np.empty(n,np.int64)

for i in range(n):
	x = MLCG(x, a)
	x = x + XORshift(x)
	xarray[i] = x*5.42101086242752217E-20

# Note: I tried to make the RNG return floating point numbers immidiately, but did not succeed.
xnorm = xarray / findNorm(xarray)
plt.scatter(xnorm,np.roll(xnorm,1))

# Test: plot sequential random numbers against each other in a scatter plot for the first 1000 numbers.
plt.title("RNG combined MLCG and XORshift n=1000, x=7")
plt.xlabel("x_(i+1)")
plt.ylabel("x_i")
plt.savefig("MLCG_XOR_n1000.png")
plt.show()

# TODO Test: generate 1,000,000 numbers and plot in 20 bins of 0.05 wide.





