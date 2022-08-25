import numpy as np
x = [0.3]
i=0
ea=100
print('iter\txi\tea')
while  ea >= 2:
    x.append(0.165-(3.993*(10**(-4))*(x[i]**-2)))
    ea=np.abs((x[i+1]-x[i])/x[i+1])*100
    print('%d\t%.4f\t%.4f'%(i+1,x[i+1],ea))
    i=i+1
print("Answer = %.4f\tea = %.2f"%(x[i],ea))

# iter    xi      ea
# 1       0.1606  86.8422
# 2       0.1495  7.3919
# 3       0.1471  1.6137
# 4       0.1466  0.3965
# 5       0.1464  0.1001
# 6       0.1464  0.0254
# 7       0.1464  0.0065
# Answer = 0.1464 ea = 0.01