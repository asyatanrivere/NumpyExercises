import numpy as np

my_1darr=np.array([1,2,3,4,5,6,7,8])
split1d=np.split(my_1darr,4)

for x in split1d:
    print(x)
"""
[1 2]
[3 4]
[5 6]
[7 8]"""

split1dforce=np.array_split(my_1darr,5)
for x in split1dforce:
    print(x)
"""
[1 2]
[3 4]
[5 6]
[7 8]
[1 2]
[3 4]
[5 6]
[7]
[8]"""
print(split1dforce[0]) # [1 2]
print(split1dforce[1]) # [3 4]
print(split1dforce[2]) # [5 6]
print("---------------------------------")

my_2darr=np.array([[1,2,3],
                   [4,5,6],
                   [7,8,9],
                   [10,11,12],
                   [13,14,15],
                   [16,17,18]])
split2d=np.split(my_2darr,3)
for x in split2d:
    print(x)
    print()
"""
[[1 2 3]
 [4 5 6]]

[[ 7  8  9]
 [10 11 12]]

[[13 14 15]
 [16 17 18]]"""

split2daxis1=np.split(my_2darr,3,axis=1)
for x in split2daxis1:
    print(x)
    print()
"""
[[ 1]
 [ 4]
 [ 7]
 [10]
 [13]
 [16]]

[[ 2]
 [ 5]
 [ 8]
 [11]
 [14]
 [17]]

[[ 3]
 [ 6]
 [ 9]
 [12]
 [15]
 [18]]"""
print("--------------------------")
splithorizontal=np.hsplit(my_2darr,3)
for x in splithorizontal:
    print(x)
    print()

"""
[[ 1]
 [ 4]
 [ 7]
 [10]
 [13]
 [16]]

[[ 2]
 [ 5]
 [ 8]
 [11]
 [14]
 [17]]

[[ 3]
 [ 6]
 [ 9]
 [12]
 [15]
 [18]]"""

splitvertical=np.vsplit(my_2darr,2)
for x in splitvertical:
    print(x)
    print()
"""
[[1 2 3]
 [4 5 6]
 [7 8 9]]

[[10 11 12]
 [13 14 15]
 [16 17 18]]"""
print("-------------------------------")
my_3darr=np.array([[[1,2,3],
                    [4,5,6]],

                   [[7,8,9],
                    [10,11,12]],

                   [[13,14,15],
                    [16,17,18]],

                   [[19,20,21],
                    [22,23,24]]])
split3d=np.dsplit(my_3darr,3)
for x in split3d:
    print(x)
"""
[[[ 1]
  [ 4]]

 [[ 7]
  [10]]

 [[13]
  [16]]

 [[19]
  [22]]]
  ****
[[[ 2]
  [ 5]]

 [[ 8]
  [11]]

 [[14]
  [17]]

 [[20]
  [23]]]
  ****
[[[ 3]
  [ 6]]

 [[ 9]
  [12]]

 [[15]
  [18]]

 [[21]
  [24]]]"""