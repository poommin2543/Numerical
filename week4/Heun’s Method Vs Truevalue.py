import numpy as np
import math
import matplotlib.pyplot as plt
import pandas
list =[]
def f(x, y) :
    """
    > The function `f` takes two arguments, `x` and `y`, and returns the value of the function
    e^{0.8x} - 0.5y$
    
    :param x: the current x value
    :param y: the initial value of y
    :return: the value of the function f(x,y)
    """
    # print(f'X = {x},Y = {y:.4f}')
    return 4*math.exp(0.8*x) - 0.5*y 

def ft(x):
    return (4/1.3)*(math.exp(0.8*x)-math.exp(-0.5*x))+2*math.exp(-0.5*x)

y0 = 2
# time step
h = 1
# solve from 0 to time T
T= 4
# list of discretized time (visualization purpose only) 
x = np.arange(0, T+h, h)
# Creating an array of zeros with the length of x.
y_h = np.zeros(len(x))
# The initial condition.
y_h[0]= y0

y_t = np.zeros(len(x)) 
y_t[0] = y0

# The Heun's method.
for i in range(1, len(x)) :
    # print("++++++++++++++++++++++++++++++++++++++++++++++++")
    #slope 1 
    s1 = f(x[i-1], y_h[i-1])
    # print(f's1 : {s1:.4f}')
    # predictor Equation
    predictor = (h * f(x[i - 1], y_h[i - 1]))+ y_h[i-1]
    # print(f'predictor : {predictor:.4f}')
    # slope 2
    s2 =  f(x[i], predictor )
    # print(f's2 : {s2:.4f}')
    # avgslope
    avgslope = ((s1+s2)/2)
    # print(f'avgslope : {avgslope:.4f}')
    #Y hueun's method
    y_h[i] = (y_h[i - 1] +avgslope )*h
    # print(f'hueun : {y_h[i]:.4f}')
    # Truevalue
    y_t[i] = ft(x[i])
    # print(f'Truevalue : {y_t[i]:.4f}')
    error = np.abs(y_t[i]-y_h[i])/y_t[i]*100
    # Appending the values of the variables to the list.
    list.append([f'{s1:.4f}',f'{s2:.4f}',f'{predictor:.4f}',f'{avgslope:.4f}',f'{y_h[i]:.4f}',f'{y_t[i]:.4f}',error])

# Creating a table with the values of the variables.
headers=["S1", "S2", "predictor", "avgslope","Y hueun","True Value","%error"]
print(pandas.DataFrame(list,columns=headers))
# Plotting the graph of the Heun's method and the true value.
plt.plot(x,y_h,label='Heun’s Method')
plt.plot(x,y_t,label='TrueValue')
plt.legend()
plt.show()