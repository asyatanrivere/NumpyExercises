import numpy as np
from numpy import random

"""
random.randint(100) -> not included 100
random.rand() -> random decimal number between 0 and 1
"""
random.seed(1) # returns same numbers when you run the code again
random1d=random.randint(100,size=(5))
print(random1d) # [37 12 72  9 75]
print("---------------------")

random2d=random.randint(100,size=(5,5))
print(random2d)
"""
[[ 5 79 64 16  1]
 [76 71  6 25 50]
 [20 18 84 11 28]
 [29 14 50 68 87]
 [87 94 96 86 13]]"""
print("---------------------")

randomdecimal1d=random.rand(5)
print(randomdecimal1d) # [0.71597052 0.8027575  0.09280081 0.51815255 0.86502025]

print("---------------------")
randomdecimal2d=random.rand(3,3)
print(randomdecimal2d)
"""
[[0.82914691 0.82960336 0.27304997]
 [0.0592432  0.67052804 0.59306552]
 [0.6716541  0.41178788 0.1975509 ]]"""

print("----------random choice from array-----------")
nums=np.array([1,2,3,4,5,6,7,8,9])
randomarr=random.choice(nums,size=8)
print(randomarr) # [9 2 5 1 4 3 1 5]

randomarr2=random.choice(nums,size=8,replace=False)
print(randomarr2) # [5 4 6 7 1 2 9 8]

randomarr3=random.choice(nums,size=(5,5))
print(randomarr3)
"""
 [7 9 1 3 8]
 [8 8 4 1 9]
 [8 8 2 2 4]
 [1 9 7 5 6]]"""
randomarr4=random.choice(nums,size=(3,3),replace=False)
print(randomarr4)
"""
[[8 1 2]
 [9 6 4]
 [5 3 7]]"""