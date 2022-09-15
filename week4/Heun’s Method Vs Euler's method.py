import numpy as np
import math
import matplotlib.pyplot as plt
# right hand side of the ODE
def f(x, y) :
    print(x,y)
    return 4*math.e**0.8*x - 0.5*y 
    #return y + 1 # x doesn't matter since dy/dx is linear

# initial condition
y0 = 2
# time step
h = 1
# solve from 0 to time T
T = 10
# list of discretized time (visualization purpose only) 
x = np.arange(0, T, h)
#x = np.linspace(0, T, T * 2)
# heun's method
y_h = np.zeros(len(x)) 
y_h[0] = y0
for i in range(1, len(x)) :
    k1 = h * f(x[i - 1], y_h[i - 1])
    k2 = h * f(x[i], y_h[i - 1] + k1)
    y_h[i] = y_h[i - 1] + (k1 + k2) / 2

# euler's method    
y_e = np.zeros(len(x)) 
y_e[0] = y0
for i in range(1, len(x)) :
    y_e[i] = y_e[i - 1] + f(x[i - 1], y_e[i - 1]) * h

#truevalue


plt.figure()

plt.plot(x, y_h, color='blue')
plt.plot(x, y_e, color='red')
plt.show()