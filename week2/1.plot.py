import matplotlib.pyplot as plt
import numpy as np
x = np.arange(-3,10,0.01)
y = (25-(4*x))/3
y2 = (-9+(6*x))/5
print(x,y,y2)
xy = x*0
plt.plot(x,y)
plt.plot(x,y2)
plt.plot(x,xy)
plt.show()
for x,y,y2 in zip(x,y,y2):
    print(x,y,y2)                            

