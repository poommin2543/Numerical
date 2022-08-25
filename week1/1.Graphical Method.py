import matplotlib.pyplot as plt
import numpy as np
xarr = []
yarr = []
y2arr = []
for x in np.arange(-3,3,0.01):
    y = (x**3)-(0.165*(x**2))+(3.993*(10**-4))
    xarr.append(x)
    yarr.append(y)
    y2arr.append(x*0)
plt.plot(xarr,yarr)
plt.plot(xarr,y2arr)
plt.show()
                            
