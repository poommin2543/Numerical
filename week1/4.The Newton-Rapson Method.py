import numpy as np
x = [0.3]
i=0
ea=100
print('iter\txi\tea')
while  ea >= 2:

    fxi = (x[i]**3)-(0.165*(x[i]**2))+(3.993*(10**-4))
    fpxi = (x[i]**2)-(0.33*x[i])

    x.append(x[i]-fxi/fpxi)
    ea=np.abs((x[i+1]-x[i])/x[i+1])*100
    print('%d\t%.4f\t%.4f'%(i+1,x[i+1],ea))
    i=i+1
print("Answer = %.4f\tea = %.2f"%(x[i],ea))

# iter    xi      ea
# 1       1.6944  82.2943
# 2       -0.2051 926.1925
# 3       -0.0669 206.6475
# 4       -0.0428 56.0829
# 5       -0.0440 2.5205
# 6       -0.0437 0.6169
# 7       -0.0437 0.1428
# 8       -0.0437 0.0335
# 9       -0.0437 0.0078
# Answer = -0.0437     ea = 0.01

