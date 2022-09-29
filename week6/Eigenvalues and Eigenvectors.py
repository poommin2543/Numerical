import numpy as np
from numpy.linalg import eig
a = np.array([[-5, 2], 
              [2, -2]])
w,v=eig(a)
print('E-value:', w)
print('E-vector', v)

a = np.array([[2, 2, 4], 
              [1, 3, 5],
              [2, 3, 4]])
w,v=eig(a)
print('E-value:', w)
print('E-vector', v)