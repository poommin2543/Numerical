clc;clear all;close all;
[x,y] = ode23('test02',[0,4],1);

x1 = 0:0.01:4;
y1 = -0.5*x1.^4+4*x1.^3-10*x1.^2+8.5*x1+1;
plot(x,y,'--',x1,y1,'r')