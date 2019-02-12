#
# Introductory test NUR
# Author: Lisa Pothoven
# Student nr: 1328263
# Date: 12 Feb 2019
#

from matplotlib import pyplot as plt
import numpy as np

numbers = range(1, 100)

# Average
def calcAverage(numbers):
	total = 0
	for num in numbers:
		total += num
	average = total/len(numbers)
	return average

# Standard deviation
def calcStandarddev(numbers, average):
	dev = 0
	for num in numbers:
		dev += (num-average)**2.
	standarddev = (dev/len(numbers))**.5
	return standarddev

average = calcAverage(numbers)
print(average)
print(calcStandarddev(numbers,average))

#Even
total = 0
counter = 0
for num in numbers:
	if (num%2 == 0):
		total += num
		counter += 1
average = total/counter
print(average)

#Odd
total = 0
counter = 0
for num in numbers:
	if (num%2):
		total += num
		counter += 1
average = total/counter
print(average)		

# c
total = 0
counter = 0
for num in numbers:
	if ((num < 10) or ((num > 20) and ((num < 45) or (num > 57)))):
		total += num
		counter += 1
average = total/counter
print(average)

# d
total = 0
counter = 0
for num in numbers:
	if (((num > 10) and (num < 20)) or ((num > 45) and (num < 57))):
		total += num
		counter += 1
average = total/counter
print(average)		
	
# e
x = np.linspace(0,3,100)
y = 0.8*np.exp(x)-2.0*x
plt.plot(x, y)
plt.show()


		



