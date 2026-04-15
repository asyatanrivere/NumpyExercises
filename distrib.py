import numpy as np
from numpy import random

random.seed(8)
arr=[2,9,13,30,25]

count2=0
count9=0
count13=0
count30=0
count25=0
for i in range(100):
    result1d=random.choice(arr,p=[0.25,0.25,0.1,0.1,0.3],size=(5))
    for item in result1d:
        if item==2:
            count2+=1
        elif item==9:
            count9+=1
        elif item==13:
            count13+=1
        elif item==30:
            count30+=1
        else:
            count25+=1
print("count of 9:",count9 )
print("count of 2:",count2 )
print("count of 13:",count13 )
print("count of 25:",count25 )
print("count of 30:",count30 )

print("probability of 2:",count2/500)
print("probability of 9:",count9/500)
print("probability of 13:",count13/500)
print("probability of 25:",count25/500)
print("probability of 30:",count30/500)
"""
count of 9: 136
count of 2: 123
count of 13: 46
count of 25: 136
count of 30: 59
probability of 2: 0.246
probability of 9: 0.272
probability of 13: 0.092
probability of 25: 0.272
probability of 30: 0.118"""

result2d=random.choice(arr,p=[0.25,0.25,0.1,0.1,0.3],size=(6,6))
print(result2d)
"""
[[ 9  9 13 25  9  2]
 [ 2 25  2  2 25 25]
 [25  2  2 30  2  9]
 [25 30  9 25  2 30]
 [30 25 25  2  9  9]
 [25  9 25  2  9 25]]"""


# shuffle changes the original array
# permutation creates a copy array
print("-------------------------------")

my_array=np.array([1,2,3,4,5,6,7,8,9])

new_array=random.permutation(my_array)
print("original:",my_array)
print("mixed:",new_array) # [6 5 7 8 9 4 2 1 3]

new_array2=random.permutation(15)
print(new_array2) # [ 5  3  0 11 12  7 10  1 13 14  2  6  9  8  4]