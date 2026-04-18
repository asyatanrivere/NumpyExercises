import numpy as np

def myMultiply(x,y):
    return x*y

myMultiply=np.frompyfunc(myMultiply,2,1)

print(myMultiply([1,2,3],[8,5,2])) # [8 10 6]
print()
print(np.isnan(np.nan)) # True      isnan -> is number      nan -> not a number
print(np.isnan(4)) # False
print()
print(np.isinf(np.inf)) # True  
print(np.isinf(5)) # False
print(np.isfinite(5)) # True
print(np.isfinite(np.inf)) # False
print()
print(np.isneginf(-np.inf)) # True 
print(np.isposinf(np.inf)) # True 
print()
print(np.isreal(7)) # True 
print(np.isreal(7j+2)) # False
print(np.iscomplex(7)) # False 
print(np.iscomplex(7j+2)) # True 
print()
print(np.signbit(4))  # False
print(np.signbit(-4))  # True
print()
print(np.isclose(0.5+3.2,3.7))  # True
print()
print(np.isscalar(3.4843))  # True
print(np.isscalar([3.4843]))  # False
print()
print()
print(np.sin(0))
print(np.sin(np.pi/2))
print()
print(np.cos(0))
print(np.cos(np.pi/2))
print()
print(np.tan(0))
print(np.tan(-np.pi/2))
print(np.tan(np.pi/2))
print()
print(np.arcsin(0))
print(np.arcsin(1))
print()
print(np.arccos(0))
print(np.arccos(1))
print()
print(np.arctan(4))
print(np.arctan(1))
print()
print(np.hypot(3,4)) # 5.0
print(np.hypot(5,12)) # 13.0
print()
degrees=np.array([45,90,180,270,360,720])
print(np.deg2rad(degrees)) # [ 0.78539816  1.57079633  3.14159265  4.71238898  6.28318531 12.56637061]
print()
radians=np.array([np.pi/2,np.pi])
print(np.rad2deg(radians)) # [ 90. 180.]
print()
print(np.sinh(1))
print(np.cosh(1))
print(np.tanh(1))
print(np.arcsinh(1.452))
print(np.arccosh(1.452))