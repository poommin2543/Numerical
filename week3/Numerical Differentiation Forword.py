#forword
#diff 1 step
def f(x):
    return -0.1*x**4 - 0.15*x**3 - 0.5*x**2 - 0.25*x + 1.2
    
x = 0.5 
h = 0.25

fx = (f(x+h)-f(x))/h

print(f(x+h),f(x))
print(fx)
#diff 2 step 

fxx = (f(x+h+h)-2*(f(x+h))+f(x))/(h**2)
print(f(x+h+h),f(x+h),f(x))
print(fxx)
