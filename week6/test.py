# Python program to inverse
# a matrix using numpy
  
# Import required package
import numpy as np
  
# Taking a 3 * 3 matrix
A = np.array([[0,10,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,1,0,0,0],
              [0,0,0,10,0,0,0,0,0],
              [0,10,0,0,1,0,0,0,0],
              [0,0,0,0,0,0,0,0,0],
              [0,0,1,0,0,0,0,0,0],
              [0,0,0,1,0,0,0,0,0],
              [0,0,0,0,1,0,0,0,0]])

arr = np.array([[1, 2, 3, 4,6,1], 
                [10, 11, 14, 25,7,2],
                [20, 8, 0, 55,1,3], 
                [40, 41, 42, 0,2,4],
                [40, 41, 0, 43,3,5], 
                [40, 41, 0, 43,3,5]])
  
# Calculating the inverse of the matrix
inv = np.linalg.inv(arr)
print(inv)
