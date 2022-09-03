import numpy as np
import matplotlib.pyplot as plt
x = 1
h = 0.5

def f(x):
    return 1-x-4*x**3+2*x**5
def Truevalues():
    return -1-12*x**2+10*x**4
def forward1step():
    return (f(x+h)-f(x))/h  
def forward2step():
    return (f(x+h+h)-2*(f(x+h))+f(x))/(h**2)
def backward1step():
    return (f(x)-f(x-h))/h
def backward2step():
    return (f(x)-2*f(x-h)+f(x-h-h))/(h**2)
def center1step():
    return (f(x+h)-f(x-h))/(2*h)
def center2step():
    return (f(x+h) - 2*f(x) + f(x-h)) / (h**2)

print(f'forward1step : {forward1step():.4f}')
print(f'forward2step : {forward2step():.4f}')
print(f'backward1step : {backward1step():.4f}')
print(f'backward2step : {backward2step():.4f}')
print(f'center1step : {center1step():.4f}')
print(f'center2step : {center2step():.4f}')

print(f'xi-2 : {x-h-h:.4f}\txi-1 : {x-h:.4f}\txi : {x:.4f}\txi+1 : {x+h:.4f}\txi+2 : {x+h+h:.4f}')

# Calculating the error of each method.
Truevalue = Truevalues()
err_foward = np.abs((forward1step() - Truevalue)/forward1step()*100)
err_backward = np.abs((backward1step() - Truevalue)/backward1step()*100)
err_center = np.abs((center1step() - Truevalue)/center1step()*100)


print(err_foward,err_backward,err_center)
# Plotting the error of each method.
plt.scatter(h, err_foward, label= "err_foward", color= "green",marker= "*", s=30)
plt.scatter(h, err_backward, label= "err_backward", color= "blue",marker= "*", s=30)
plt.scatter(h, err_center, label= "err_center", color= "red",marker= "*", s=30)
# x-axis label
plt.xlabel('H')
# frequency label
plt.ylabel('%error')

plt.legend()
plt.show()