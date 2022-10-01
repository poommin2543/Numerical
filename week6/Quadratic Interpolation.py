
# Finding the coefficients of the quadratic polynomial that interpolates the points (x0,fx0),
# (x1,fx1), and (x2,fx2).
x0 = 1
x1 = 4 
x2 = 6
fx0 = 0
fx1 = 1.386294
fx2 = 1.791759

b0 = fx0
b1 = (fx1-b0)/(x1-x0)
b2 = (((fx2-fx1)/(x2-x1))- b1)/(x2-x0)

a0 = b0 -b1*x0 + b2*x0*x1
a1 = b1 - b2*x0 - b2*x1
a2 = b2

#f2(x) = a0 +a1x+a2x^2
x = 2
fx = a0 + a1*x +a2*x**2

print(fx) 