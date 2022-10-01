clc;clear all;close all;
[x,y] = ode23('test02',[0,4],1);
plot(x,y)