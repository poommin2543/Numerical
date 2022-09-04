import numpy as np
import pandas
import matplotlib.pyplot as plt
trueValue = 1.640533
n = 5
a = 0
b = 0.8
n = n+1
listTable = []
listError = []
listN = []
listO = []
for n in range(2,n+1):
    # print(n)
    if (n-1==0):
        h = 0
    else:
        h = (b - a) / (n-1)
    x = np.linspace(a, b, n)
    #function
    f = 0.2+25*x-200*x**2+675*x**3-900*x**4+400*x**5
    # print(f)
    I_trap = (h/2)*(f[0] + 2 * sum(f[1:n-1]) + f[n-1])
    err_trap = (np.abs(trueValue-I_trap)/trueValue)*100
    listN.append(n-1)
    listError.append(err_trap)
    listTable.append([n-1,f'{h:.4f}',f'{I_trap:.4f}',f'{err_trap:.4f}'])
    listO.append(0)
    # print(I_trap)
    # print(err_trap)
    # print(f'n:{n-1}\th:{h:.4f}\tI:{I_trap:.4f}\terr:{err_trap:.4f}')

#printTable
# Printing the table with the headers.
headers=["N", "H", "I_trap", "err_trap"]
print(pandas.DataFrame(listTable,columns=headers))

# Plotting the graph of N vs %Error.
plt.plot(listN,listError,color='red')
plt.plot(listN,listO)
plt.ylabel('%Error')
plt.xlabel('N')
plt.title(label="N vs %Error chart",
          fontsize=20)
plt.show()

# A table of the results.
# N       H  I_trap  err_trap
# 0  1  0.8000  0.1728  849.3825
# 1  2  0.4000  1.0688   53.4930
# 2  3  0.2667  1.3696   19.7842
# 3  4  0.2000  1.4848   10.4885
# 4  5  0.1600  1.5399    6.5364