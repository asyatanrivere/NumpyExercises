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

arrf4 = np.array([2.543,97.35434],dtype= "f4")
arrf8 = np.array([2.5443533,97.3235255434],dtype= "f8")
print(arrf4) # [ 2.543   97.35434]
print(arrf4.dtype) # float32
print(arrf8) # [ 2.5443533  97.32352554]
print(arrf8.dtype) # float64

arru1=np.array([100,200], dtype="u1") # unsigned bit is 8 bit and it's between 0 and 255
                                      # 256 is too big
                                      # just positive numbers
arru4=np.array([100,800], dtype="u4")
print(arru1) # [100 200]
print(arru1.dtype) # uint8
print(arru4) # [100 800]
print(arru4.dtype) # uint32

arrs=np.array([b"hello",b"python"], dtype="S") # byte string -> ASCII
                                               # byte string -> byte string (ü,ö,ş,i etc are unvalid)
                                               # string -> UNICODE (str)                                             
print(arrs) # [b'hello' b'python']
print(arrs.dtype) # |S6
arrs5=np.array([b"hello",b"python"], dtype="S5") # max 5 character
print(arrs5) # [b'hello' b'pytho']
print(arrs5.dtype) # |S5

arrb=np.array([True,False], dtype="b")
print(arrb) # [1 0]
print(arrb.dtype) # int8

arro=np.array([2,43.2375,"Asya",[2,53,2],True], dtype="object")
print(arro) # [2 43.2375 'Asya' list([2, 53, 2]) True]
print(arro.dtype) # object

arrdate=np.array(["2004-11-18","1938-10-29"], dtype="M8[D]")
print(arrdate) # ['2004-11-18' '1938-10-29']
print(arrdate.dtype) # datetime64[D]