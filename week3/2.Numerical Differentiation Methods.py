x = 0.25 
h = 0.1

def f(x):
    return -0.1*x**4 - 0.15*x**3 - 0.5*x**2 - 0.25*x + 1.2
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

print(f'forward1step : {forward1step()}')
print(f'forward2step : {forward2step()}')
print(f'backward1step : {backward1step()}')
print(f'backward2step : {backward2step()}')
print(f'center1step : {center1step()}')
print(f'center2step : {center2step()}')

print(f'xi-2 : {x-h-h:.4f}\txi-1 : {x-h:.4f}\txi : {x:.4f}\txi+1 : {x+h:.4f}\txi+2 : {x+h+h:.4f}')


