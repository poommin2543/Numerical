import numpy as np
trueValue = 1.640533
n = 5
a = 0
b = 0.8
n = n+1
for n in range(2,n+1):
    # print(n)
    if (n-1==0):
        h = 0
    else:
        h = (b - a) / (n-1)

    x = np.linspace(a, b, n)
    # print(x)
    # print(h)
    #function
    f = 0.2+25*x-200*x**2+675*x**3-900*x**4+400*x**5
    print(f)
    I_trap = (h/2)*(f[0] + 2 * sum(f[1:n-1]) + f[n-1])
    err_trap = (np.abs(I_trap-trueValue)/I_trap)*100

    # print(I_trap)
    # print(err_trap)
    print(f'n:{n-1}\th:{h:.4f}\tI:{I_trap:.4f}\terr:{err_trap:.4f}')