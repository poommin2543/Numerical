import numpy as np
xl=0.055
xu=0.070
i=1
ea=100
xro=0  #xr from i-1 iteration
while ea>=2:
    fxl=(xl**3)-(0.165*(xl**2))+(3.993*(10**-4))
    fxu=(xu**3)-(0.165*(xu**2))+(3.993*(10**-4))
    xr=xu-fxu*(xl-xu)/(fxl-fxu)
    fxr = (xr**3)-(0.165*(xr**2))+(3.993*(10**-4))
    ea = np.abs((xr-xro)/xr)*100
    print(f'{i} {xl} {xr} {xu}  {ea} %')
    if fxl*fxr>0:
        xl=xr
    elif fxl*fxr<0:
        xu=xr
    else:
        print(f"Root of Equation is {xr}")
        break
    xro=xr
    i=i+1
print(f"Root of Equation is {xr}")

# 1 -0.046 -0.04367971670273461 -0.042 %error = 100.0 %
# 2 -0.046 -0.04373522636637265 -0.04367971670273461 %error = 0.12692209061188967 %
# Root of Equation is -0.04373522636637265
# xl=-0.046
# xu=-0.040

# 1 0.055 0.06251977401129943 0.07 %error = 100.0 %
# 2 0.055 0.06237931439113949 0.06251977401129943 %error = 0.22517018907777217 %
# Root of Equation is 0.06237931439113949

# 1 0.14 0.14594754098360657 0.15 %error = 100.0 %
# 2 0.14594754098360657 0.14633483948199122 0.15 %error = 0.2646659536140813 %
# Root of Equation is 0.14633483948199122
# xl=0.140
# xu=0.150
