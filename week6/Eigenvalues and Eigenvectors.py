import numpy as np
from numpy.linalg import eig
a = np.array([[-5, 2], 
              [2, -2]])
w,v=eig(a)
print('E-value:', w)
print('E-vector', v)

a = np.array([[1, 2, 3], 
              [0, 5, 6],
              [0, 0, 1]])
w,v=eig(a)
print('E-value:', w)
print('E-vector', v)