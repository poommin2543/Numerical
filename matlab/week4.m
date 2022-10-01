clc;clear all;close all;


% while true
%     T = input('Noom = ');
%     %disp(T)
%     %disp("Noom")
%     
%     if T>=40
%         pump = 1;
%     else
%         pump = 0;
%     end
%     disp(pump)
%     break
% end

% for i = 1:1:2 %start:step:stop
%     T = input('Noom = ');
%     
%     if T>=40
%         pump = 1;
%     else
%         pump = 0;
%     end 
%     disp(pump)
% %     break
% end

% x = 10;
% y = 20;
% a = noomFunction(x,y);
% disp(a)


% y = x^2+2x+1;
%สูงไปต่ำ(หาค่าx)
% roots([1 2 1])

% y = x^4-12x^3+25x+116=0
% roots([1 -12 0 25 116])


x = 10;
y = 20;
a = noomFunction1(x,y);
disp(a)
%function
function arr = noomFunction1(x,y)
arr = x+y;
end


