import numpy as np

arr=np.array(1)
arr1=np.array([1,2,3])
arr2=np.array([[1,2,3],[4,5,6],[7,8,9]])
arr3=np.array([[[1,2,3],[4,5,6],[7,8,9]],[[10,11,12],[13,14,15],[16,17,18]],[[19,20,21],[22,23,24],[25,26,27]]])
arr4=np.eye(5,5) # diagonal matrix
arr5=np.array([2,5,3],ndmin=8)
print("number of dimension:",arr.ndim) 
print("number of dimension:",arr1.ndim) 
print("number of dimension:",arr2.ndim) 
print("number of dimension:",arr3.ndim) 
print("number of dimension:",arr5.ndim)
print(arr3)
"""
[[[ 1  2  3]
  [ 4  5  6]
  [ 7  8  9]]

 [[10 11 12]
  [13 14 15]
  [16 17 18]]

 [[19 20 21]
  [22 23 24]
  [25 26 27]]]
  """
print("\n")
print("diagonal with eye method:\n",arr4)

arraran=np.arange(0,21,1) # not include 21
arraran1=np.arange(0,21,2)
print(arraran)
print(arraran1)

print("\n")

arrzeros=np.zeros((4,4)) # 4*4 zero matrix
print(arrzeros)

arrone=np.ones((3,3))
print(arrone)

arrlin=np.linspace(0,1,5)
print("array with methof of linspace:\n",arrlin) #  [0.   0.25 0.5  0.75 1.  ]

print("\n")

arrtwos=np.full((3,10),2) # 3*10 matrix with all entries with 2
print("array with full of 2:\n",arrtwos)

print("\n")

arrem=np.empty((4,5)) # random entries from ram
print("arr with empty method:\n",arrem)


arrexam=np.array(
                  [[1,2,3],
                   [4,5,6],
                   [7,8,9]]
                   )
print(arrexam[:,2]) # [3 6 9]
print(arrexam[1,:]) # [4 5 6]
print(arrexam[arrexam<6]) # [1 2 3 4 5]
print(arrexam[:,0]) # [1 4 7]
print(arrexam[2]) # [7 8 9]
print(arrexam[:2,1:]) # [[2 3]
                      # [5 6]]
print(arrexam[1:,1:]) # [[5 6]
                      #[8 9]]
print(arrexam[:,:2]) # [[1 2]
                     # [4 5]
                     # [7 8]]
print("--------------")
arr1d=np.array([3,8,5,12,56,32,2])
print(arr1d[:5:2]) # [ 3  5 56]
arr3d=np.array([
    [[1,2,3],
     [4,5,6]],
     
     [[7,8,9],
      [10,11,12]],
      
      [[13,14,15],
       [16,17,18]]])

print(arr3d[2,0,1]) # 14
print(arr3d[2,:,1:]) # [[14 15]
                     # [17 18]]
