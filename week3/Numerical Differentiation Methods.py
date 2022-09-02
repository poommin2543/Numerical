import numpy as np
import matplotlib.pyplot as plt
 
def f(x):
 return (x**2)+2*x+1
 
x = np.arange(0,4,0.01)
print(x)
y = f(x)
# print(y)
# plt.figure(figsize=(10,5))
# plt.plot(x, y, 'b')
# plt.grid(axis = 'both')
# plt.show()

# https://docs.scipy.org/doc/scipy-0.18.0/reference/generated/scipy.misc.derivative.html
#
from scipy.misc import derivative
 
d = derivative(f, 1.0, dx=1e-3)
 
# print (d)

dy = np.gradient(y)
dx = np.gradient(x)
 
d = dy/dx
# print(y,x)
