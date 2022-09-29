# Python3 code
# Implementing Linear interpolation
# Creating Function to calculate the
# linear interpolation
# loge(x) or ln(x)


# Importing the numpy library and assigning the log function to a new function called ln.
import numpy as np
from math import e
ln = np.log  # assign the numpy log function to a new function called ln
print(ln(e))
print(ln(6))


def interpolation(d, x):
	# output = d[0][1] + (x - d[0][0]) * ((d[1][1] - d[0][1])/(d[1][0] - d[0][0]))
	output = d[0][1] + (d[1][1] - d[0][1]) * ((x - d[0][0])/(d[1][0] - d[0][0]))

	return output

# Driver Code
data=[[1, 0],[6, 1.791759]]

Goal=2

# Finding the interpolation
print("Answer {} is".format(Goal),interpolation(data, Goal))

#Error
error = np.abs(ln(Goal)-interpolation(data, Goal))/ln(Goal)*100
print(error)

#multi

# Implementation of Linear Interpolation using Python3 code
# Importing library

# from scipy.interpolate import interp1d
 
# X = [1,2,3,4,5] # random x values
# Y = [11,2.2,3.5,-88,1] # random y values
 
# # test value
# interpolate_x = 2.5
 
# # Finding the interpolation
# y_interp = interp1d(X, Y)
# print("Value of Y at x = {} is".format(interpolate_x),
#       y_interp(interpolate_x))