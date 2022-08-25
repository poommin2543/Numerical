# Gauss Seidel Iteration
import pandas
# Defining equations to be solved
# in diagonally dominant form
f1 = lambda x,y,z: (9-(2*y)-(3*z))
f2 = lambda x,y,z: (24-(4*x)-(6*z))/5
f3 = lambda x,y,z: (4-(3*x)-y)/-2
list = []
# Initial setup
x0 = 0
y0 = 0
z0 = 0
count = 0

# Reading tolerable error
# e = float(input('Enter tolerable error: '))
e = 0.01
# Implementation of Gauss Seidel Iteration
# print('\nCount\tx\t\ty\t\tz\t\terrorx\t\terrory\t\terrorz\n')
# x1 = f1(x0,y0,z0)
# y1 = f2(x1,y0,z0)
# z1 = f3(x1,y1,z0)
condition = True
# print(x1,y1,z1)
while condition:
    x1 = f1(x0,y0,z0)
    y1 = f2(x1,y0,z0)
    z1 = f3(x1,y1,z0)
    e1 = (abs(x0-x1)/x1)*100
    e2 = (abs(y0-y1)/y1)*100
    e3 = (abs(z0-z1)/z1)*100
    list.append([count,f'{x1:.4f}',f'{y1:.4f}',f'{z1:.4f}',f'{e1:.4f}',f'{e2:.4f}',f'{e3:.4f}'])
    # print(f'{count}\t{x1:.4f}\t{y1:.4f}\t{z1:.4f}\t{e1:.4f}\t{e2:.4f}\t{e3:.4f}\t')
    # print('%d\t%0.4f\t%0.4f\t%0.4f\n' %(count, x1,y1,z1))
    # print('%d\t %.4f\t %.4f\t %.4f\t%.4f\t%.4f\t%.4f\n' %(count, x1,y1,z1,e1,e2,e3))
    # print(e1,e2,e3)
    count += 1
    x0 = x1
    y0 = y1
    z0 = z1
    if count == 15:
        break
    # condition = e1>e and e2>e and e3>e
# print(list)
headers=["Count", "X", "Y", "Z","ErrorX","ErrorY","ErrorZ"]
# docnames = ["Doc " + str(i) for i in range(len(list))]
# print(docnames)
print(pandas.DataFrame(list,columns=headers))
# print('\nSolution: x=%0.3f, y=%0.3f and z = %0.3f\n'% (x1,y1,z1))
