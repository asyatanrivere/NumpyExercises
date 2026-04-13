import numpy as np

x= np.array([1,2,3,4])
y= np.array([5,6,7,8])
result=np.concatenate((x,y)) # tuple
                             # default axis=0

print(result) # [1 2 3 4 5 6 7 8]
print(result.shape) # (8,)

print(20*"1-")

x_2d=np.array([[1,2,3],[4,5,6]])
y_2d=np.array([[7,8,9],[10,11,12]])

print(np.concatenate((x_2d,y_2d),axis=0))
"""
[[ 1  2  3]
 [ 4  5  6]
 [ 7  8  9]
 [10 11 12]]"""
print(np.concatenate((x_2d,y_2d),axis=1))
"""[[ 1  2  3  7  8  9]
 [ 4  5  6 10 11 12]]"""
print(20*"2-")

#x= np.array([1,2,3,4])
#y= np.array([5,6,7,8])

stackxy=np.stack((x,y)) # default axis=0
print(stackxy) # [[1 2 3 4]
               # [5 6 7 8]]
print(stackxy.shape) # (2, 4)
stackxy2=np.stack((x,y),axis=1)
print(stackxy2) # [[1 5]
                # [2 6]
                # [3 7]
                # [4 8]]
print(stackxy2.shape) # (4, 2)

hstackxy=np.hstack((x,y))
print(hstackxy) # [1 2 3 4 5 6 7 8]
print(hstackxy.shape) # (8,)

hstackxy2d=np.hstack((x_2d,y_2d))
print(hstackxy2d)
"""[[ 1  2  3  7  8  9]
 [ 4  5  6 10 11 12]]"""
print(hstackxy2d.shape) # (2, 6)
print(20*"3-")

vstackxy=np.vstack((x,y))
print(vstackxy) # [[1 2 3 4]
                # [5 6 7 8]]
print(vstackxy.shape) # (2, 4)

vstackxy2d=np.vstack((x_2d,y_2d))
print(vstackxy2d)
"""[[ 1  2  3]
 [ 4  5  6]
 [ 7  8  9]
 [10 11 12]]"""
print(vstackxy2d.shape) #(4, 3)

print(20*"4-")

dstackxy2d=np.dstack((x_2d,y_2d))
print(dstackxy2d)
"""[[[ 1  7]
  [ 2  8]
  [ 3  9]]

 [[ 4 10]
  [ 5 11]
  [ 6 12]]]"""
print(dstackxy2d.shape) # (2, 3, 2)
print(20*"5-")

columnstack=np.column_stack((x,y))
print(columnstack)
"""[[1 5]
 [2 6]
 [3 7]
 [4 8]]"""
print(columnstack.shape) # (4, 2)