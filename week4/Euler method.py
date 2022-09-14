#TinstOrderODE
#Euler'sMethod
import matplotlib.pyplot as plt
import numpy as np
x=[0]
y=[1]
yt=[1]
h=0.5
i=0 #xStart
xEnd = 4
print('x[i]\t\ty_true\t\ty[i]\tet')
while x[i]<=xEnd-h:
    x.append(x[i]+h)
    y.append(y[i]+(-2*x[i]**3+12*x[i]**2-20*x[i]+8.5)*h)
    yt.append(-0.5*x[i+1]**4+4*x[i+1]**3-10*x[i+1]**2+8.5*x[i+1]+1)
    et=np.abs((yt[i+1]-y[i+1])/yt[i+1])*100
    print('%.4f\t%10.4f\t%10.4f\t%.2f'%(x[i+1],yt[i+1],y[i+1],et))
    i=i+1
plt.plot(x,y,label='Euler')
plt.plot(x,yt,label='True')
plt.legend()
plt.show()