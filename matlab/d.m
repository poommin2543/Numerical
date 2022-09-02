clc; clear all;
x1 = -10:00.1:10;
x2 = -10:00.1:10;
[x1,x2] = meshgrid(x1,x2);
a = ((sin(sqrt((x1.^2) + (x2.^2))).^2)-0.5);
b = (1+0.001*((x1.^2)+(x2.^2))).^2;
z = 0.5+a./b

%[x1,x2,Z]=peaks(15)
mesh(x1,x2,z);
