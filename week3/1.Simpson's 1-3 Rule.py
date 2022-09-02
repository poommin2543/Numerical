import numpy as np
import pandas
import matplotlib.pyplot as plt
trueValue = 1.640533
a = 0
b = 0.8
n = 10
n = n+1
listTable = []
listError = []
listN = []
for n in range(2,n+1):
    # print(n)
    h = (b - a) / (n - 1)
    x = np.linspace(a, b, n)
    # print(x)
    f = 0.2+25*x-200*x**2+675*x**3-900*x**4+400*x**5
    # print(f)
    # print(f[1:n-1:2])
    I_simp = (h/3) * (f[0] + 2*sum(f[2:n:2])+ 4*sum(f[1:n-1:2]) + f[n-1])
    err_simp = (np.abs(I_simp-trueValue)/I_simp)*100
    listN.append(n-1)
    listError.append(err_simp)
    listTable.append([n-1,f'{h:.4f}',f'{I_simp:.4f}',f'{err_simp:.4f}'])

    # print(h)

#printTable
headers=["N", "H", "I_trap", "err_trap"]
print(pandas.DataFrame(listTable,columns=headers))

# print(listError)
#plots
plt.plot(listN,listError,color='red')
plt.ylabel('%Error')
plt.xlabel('N')
plt.title(label="N vs %Error chart",
          fontsize=20)
plt.show()