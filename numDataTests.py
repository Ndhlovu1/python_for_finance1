import numpy as np

#Numpy has strong Array usages that store multiple data 
#This data is then worked on by the numpy ()

#Array allows for easy data calculation
prices = [42.8, 102.03, 240.38, 80.9]

#Returns average value of the array
print(np.mean(prices))

#returns the standard deviation, a measure of how dispersed the data is in relation to the mean
print(np.std(prices))

#returns the sum of all numbers
print(np.sum(prices))

#returns the maximum value in the array
print(np.max(prices))


