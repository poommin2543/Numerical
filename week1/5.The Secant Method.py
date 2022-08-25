import numpy as np
x = [0,1]
i=1
ea=100
print('iter\txi\tea')
while  ea > 2:
    fxi = (x[i]**3)-(0.165*(x[i]**2))+(3.993*(10**-4))
    fxi1 = (x[i-1]**3)-(0.165*(x[i-1]**2))+(3.993*(10**-4))

    x.append(x[i]-fxi*(x[i-1]-x[i])/(fxi1-fxi))
    ea=np.abs((x[i+1]-x[i])/x[i+1])*100
    print('%d\t%.4f\t%.4f'%(i+1,x[i+1],ea))
    i=i+1
print("Answer = %.4f\tea = %.2f"%(x[i],ea))

# iter    xi      ea
# 2       -0.0005 209215.9529
# 3       -0.0010 50.0096
# 4       -1.6756 99.9429
# 5       -0.0011 154204.5609
# 6       -0.0012 10.6412
# 7       -1.0413 99.8833
# 8       -0.0015 67846.0402
# 9       -0.0018 17.1436
# 10      -0.7055 99.7378
# 11      -0.0025 28150.7142
# 12      -0.0031 20.5574
# 13      -0.4197 99.2510
# 14      -0.0048 8731.2681
# 15      -0.0063 25.1136
# 16      -0.2103 96.9824
# 17      -0.0112 1782.6189
# 18      -0.0157 28.8685
# 19      -0.0869 81.9349
# 20      -0.0293 196.7317
# 21      -0.0370 20.8507
# 22      -0.0456 18.8559
# 23      -0.0435 4.7548
# 24      -0.0437 0.4354
# Answer = -0.0437       ea = 0.44