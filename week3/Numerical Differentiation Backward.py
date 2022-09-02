#backward
#diff 1 step
def f(x):
    return -0.1*x**4 - 0.15*x**3 - 0.5*x**2 - 0.25*x + 1.2

x = 0.5 
h = 0.25

fx = (f(x)-f(x-h))/h

print(fx)

#diff 2 step
print(f(0))

fxx = (f(x)-2*f(x-h)+f(x-h-h))/(h**2)
print(fxx)