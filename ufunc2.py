import numpy as np

functrunc=np.trunc([3.4567,-3.9967]) # numpy function - faster
print(functrunc) # [ 3. -3.]
funcfix=np.fix([3.4567,-3.9967]) # python function
print(funcfix) # [ 3. -3.]
funcaround=np.around(6.41784,3)
print(funcaround) # 6.418
funcrint=np.rint(6.41784)
print(funcrint) # 6.0
funcrint2=np.rint(6.51784)
print(funcrint2) # 7.0
funcfloor=np.floor(3.4845)
funcfloor2=np.floor(3.9845)
print(funcfloor) # 3.0
print(funcfloor2) # 3.0
funcceil=np.ceil(3.4845)
funcceil2=np.ceil(3.9845)
print(funcceil) # 4.0
print(funcceil2) # 4.0
funxexp=np.exp(1) # e^x
print(funxexp) # 2.718281828459045
funcexp2=np.exp2(4) # 2^x
print(funcexp2) # 16.0
funcexpm1=np.expm1(1e-6) # e(x)-1 ----> 10^(-6)
print(funcexpm1) # 1.0000005000001667e-06
funclog2=np.log2(32)
print(funclog2) # 5.0
funclog10=np.log10(1000)
print(funclog10) # 3.0
funclog=np.log(np.e) # ln function
print(funclog) # 1.0
funclog1p=np.log1p(1e-7) 
print(funclog1p) # 9.999999500000032e-08
funclogaddexp=np.logaddexp(2,5) # log(e^2 + e^5)
print(funclogaddexp) # 9.999999500000032e-08
np.logaddexp2(3,4)
funclogaddexp2=np.logaddexp2(3,4) # log2(2^x + 2^y)
print(funclogaddexp2) # 4.584962500721156