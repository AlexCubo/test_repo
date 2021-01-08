#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#%%
import matplotlib.pyplot as plt 

#Task 1: Read data values from datapoints.csv file
xs, ys = [], []
with open('datapoints.csv') as dataFile:
    dataFile.readline() #ignore header
    for line in dataFile:
        x, y = line.split(',')
        xs.append(float(x))
        ys.append(float(y))
      
#Task 2: create a scatter plot of the data
plt.title('y points vs x')
plt.xlabel('x')
plt.ylabel('y')
plt.plot(xs, ys, 'ko', label = 'Raw data')

#Task 3: calculate a fit y = 10x + 0
a = 10
b = 0
yFits = []
for x in xs:
    yFit = a * x + b
    yFits.append(yFit)
#plt.plot(xs, yFits, 'k-', label = 'Fitting (y=10x)')

mse = 0.0

#Task 4: Mean Squared Error
def mse(preds, trues):
    '''Assume preds and trues lists of same length
       containing floats. 
       Returns the Mean Squared Error.'''
    MSE = 0.0
    for i in range(len(preds)):
        MSE += (preds[i] - trues[i]) ** 2   
    return MSE/len(xs)

MSEinit = mse(yFits, ys)
print('Initial MSE = ', MSEinit)

#Task 5: Best slop (with b = 0)
numTrials = 100
minMSE = MSEinit
for i in range(numTrials):
    newyFits = []
    a -= 0.1
    for x in xs:
        newyFit = a * x + b
        newyFits.append(newyFit)
    MSE = mse(newyFits, ys)
    if MSE <= minMSE:
        minMSE = MSE
        aOpt = a
        bestFits = newyFits[:]
print('MSE =', minMSE, '(a = ' +str(round(aOpt,2))+ ', b = 0)')
#plt.plot(xs, bestFits, 'b-', \
#    label = 'Fitting (y=' +str(round(aOpt,2))+ 'x)')

# Task 6: Modification of "a" and "b" to find the
#         optimal fitting
optMSE = MSEinit
a = 10
for i in range(numTrials):
    b = 0
    for b in range(numTrials):
        newyFits = []
        b += 0.1
        for x in xs:
            newyF = a * x + b
            newyFits.append(newyF)
        MSE = mse(newyFits, ys)
        if MSE < optMSE:
            optMSE = MSE
            aOpt, bOpt = a, b
            optFits = newyFits[:]
    a -= 0.1

print('MSE =', optMSE, '(a = ' +str(round(aOpt,2))+ 
    ', b = ' +str(round(bOpt,3))+ ')')
#plt.plot(xs, optFits, 'r-', \
#label = 'Fitting (y=' +str(round(aOpt,2))+ 'x+' +str(bOpt)+ ')')

# Task 7: Optimization of the algorithm:

# First Idea (Implemented below, please uncomment):
# Reducing the search for the best fit to a single for loop.
# The optimal fitting line passes through the point (meanx, meany)
# (i.e the balance point) --> we can write the fitting line
# as a*(x-meanx)+meany and then searching just for the optimal slope
# (since the intercept is expressed as function of the slope).

# Second idea:
# Starting from a smaller slope and iterating a smaller number of times.
# Analyzing the raw data, one can see that the values are spread
# almost flat around values ymin = 0.01963 and ymax 2.998 -->
# One can think to start from a slope a = 4 and reduce it up to
# a = 0. The same way, for the loop for "b", one can start from
# b = 0 and increase it up to b = 3.
'''
meany = 0.0
for y in ys:
    meany += y
meany = meany/len(ys)

meanx = 0
for x in xs:
    meanx += x
meanx = meanx/len(xs)

minMSE = MSEinit
a = 4
numIt = 0
while a >= 0:
    newyFits = []
    a -= 0.1
    for x in xs:
        newyFit = a * (x - meanx) + meany
        newyFits.append(newyFit)
    MSE = mse(newyFits, ys)
    if MSE <= minMSE:
        minMSE = MSE
        aOpt = a
        bestFits = newyFits[:]
bOpt = meany - a * meanx
print('MSE =', optMSE, '(a = ' +str(round(aOpt,2))+ 
    ', b = ' +str(round(bOpt,3))+ ')')
plt.plot(xs, bestFits, 'g-', \
label = 'Fitting (y=' +str(round(aOpt,2))+ 'x+' +str(round(bOpt,4))+ ')')
'''
plt.legend(loc = 'best')




# %%

# %%
