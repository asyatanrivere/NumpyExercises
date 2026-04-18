import numpy as np

x=np.array([2,5,7])
y=np.array([3,6,9])
print(np.sum([x,y])) # 32
print(np.sum([x,y],axis=1)) # [14 18]
print(np.cumsum(x)) # [ 2  7 14]
print(np.cumsum(y)) # [ 3  9 18]
print(np.prod(x)) # 70
print(np.prod(y)) # 162
print(np.prod([x,y],axis=1)) # [ 70 162]
print(np.prod([x,y])) # 11340
print(np.cumprod(x)) # [ 2 10 70]
print(np.cumprod(y)) # [  3  18 162]
print(np.cumprod([x,y])) # [    2    10    70   210  1260 11340]
print(np.cumprod([x,y],axis=1)) 
"""
[[  2  10  70]
 [  3  18 162]]"""

arrdiff=np.array([32,5,23,8,84,43,11])
print(np.diff(arrdiff)) # [-27  18 -15  76 -41 -32]
print(np.diff(arrdiff,n=2)) # [  45  -33   91 -117    9]
print()

arrlcm=([3,5,30,2])
arrgcd=([196,24,400])
print(np.lcm(36,4)) # 36
print(np.lcm.reduce(arrlcm)) # 30
print(np.gcd(15,6)) # 3
print(np.gcd.reduce(arrgcd)) # 4
print()

set1=np.array([1,1,1,1,4,4,4,4,3,3,3,7,9,9,9,5,4,3,2,8,8,13])
set2=np.array([1,1,1,4,12,11,12,12,12,0,0,0,7,9,5,4,3,2,8,1,2,14])

print(np.unique(set1)) # [ 1  2  3  4  5  7  8  9 13]
print(np.unique(set2)) # [ 0  1  2  3  4  5  7  8  9 11 12 14]
print(np.union1d(set1,set2)) # [ 0  1  2  3  4  5  7  8  9 11 12 13 14]
print(np.intersect1d(set1,set2)) # [1 2 3 4 5 7 8 9]
print(np.intersect1d(set1,set2,assume_unique=True)) # [ 0  0  1  1  1  1  1  1  1  2  2  3  3  3  3  4  4  4  4  4  4  5  7  8  8  9  9  9 12 12 12]
print()
print(np.setdiff1d(set1,set2)) # [13]
print(np.setxor1d(set1,set2)) # [ 0 11 12 13 14] -> not common ones
