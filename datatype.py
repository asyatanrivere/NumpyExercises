import numpy as np
arr1=np.array([5.375026,2.938295,23.272418],dtype=np.float32)
print(arr1)
print(arr1.dtype)

arr2=np.array([23.37543026,732.93678295,2321.27245318],dtype=np.float64)
print(arr2)
print(arr2.dtype)

arr3=np.array([3.14,6.34,9.28,29.10],dtype=np.float16)
print(arr3)
print(arr3.dtype)

arrstr=np.array(["Asya","Tanrıvere"])
print(arrstr.dtype) # <U9 -> character number of the longest string (Tanrıvere)

arrbool= np.array([True,False])
print(arrbool.dtype) # bool

arrchange=np.array([43,1,0,6])
newarrchanged=arrchange.astype(bool)
print(newarrchanged) # [ True  True False  True]
print(newarrchanged.dtype) # bool

arri=np.array([2.2432341,5.9035803,32.895830853], dtype="i") # i4
arri8=np.array([2.2432341,5.9035803,32.895830853], dtype="i8")
print(arri) # [ 2  5 32]
print(arri.dtype) # int 32
print(arri8) # [ 2  5 32]
print(arri8.dtype) # int64