x = 0.5 
h = 0.25

def f(x):
    return -0.1*x**4 - 0.15*x**3 - 0.5*x**2 - 0.25*x + 1.2
def forward1step(x):
    return (f(x+h)-f(x))/h  
def forward2step(x):
    return (f(x+h+h)-2*(f(x+h))+f(x))/(h**2)
def back


