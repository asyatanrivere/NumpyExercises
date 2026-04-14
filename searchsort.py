import numpy as np

arr1=np.array([4,7,3,4,0,7,6,1,4,4,7,2,9,8,1])

equalsto4=np.where(arr1==4)
print(equalsto4) # (array([0, 3, 8, 9]),)

gretaerthan5=np.where(arr1>5)
print(gretaerthan5) # (array([0, 3, 8, 9]),)

evennumbers=np.where(arr1%2==0)
print(evennumbers) # (array([0, 3, 8, 9]),)

for x in evennumbers:
    print(x)
    # [ 0  3  4  6  8  9 11 13]

boolenmaybe=np.where(arr1==False)
print(boolenmaybe) # (array([4]),) False which means that value is 0
print("-----------------------------")

arr2_1=np.array([1,7,2,9,0,5,3,1,5,8,0,4])
arr2_2=np.array([1,2,3])
isin=np.isin(arr2_1,arr2_2)
print(isin)
# [ True False  True False False False  True  True False False False False]
#     1,   7,     2,   9,    0,    5,     3,    1,   5,    8,    0,    4

nonzero=np.nonzero(arr2_1)
print(nonzero) # (array([ 0,  1,  2,  3,  5,  6,  7,  8,  9, 11]),)
print("-------------------------------")

arr=np.array([3,76,52,86,45,5,13,7,34])
print(np.argmax(arr)) # 3
print(np.argmin(arr)) # 0
print("--------------------------------")

sarr=np.array([2,5,7,9,11,14,35,66,72]) # must be already sorted
print(np.searchsorted(sarr,9))              # 3
print(np.searchsorted(sarr,9,side="right")) # 4
print(np.searchsorted(sarr,[7,14,35]))      # [2 5 6]

print("---------------------------------")
# arr=np.array([3,76,52,86,45,5,13,7,34])
print(arr)          # [ 3 76 52 86 45  5 13  7 34]
print(np.sort(arr)) # [ 3  5  7 13 34 45 52 76 86]
# does not change the original array

strarray=np.array(["latte","americano","cortado","espresso","mocha","flat white"])
print(strarray)
print(np.sort(strarray))
"""
['latte' 'americano' 'cortado' 'espresso' 'mocha' 'flat white']
['americano' 'cortado' 'espresso' 'flat white' 'latte' 'mocha']"""

boolarray=np.array([True,False,True,True])
print(boolarray)
print(np.sort(boolarray))
"""
[ True False  True  True]
[False  True  True  True]"""
print("------------------------------")

arr2d=np.array([[7,23,5],
                [4,34,85],
                [91,6,48]])
sortedarr1=np.sort(arr2d) # default axis is -1 -> row based sorting
sortedarr2=np.sort(arr2d,axis=0) # column based sorting

print(arr2d)
"""
[[ 7 23  5]
 [ 4 34 85]
 [91  6 48]]"""
print(sortedarr1)
"""
[[ 5  7 23]
 [ 4 34 85]
 [ 6 48 91]]"""
print(sortedarr2)
"""
[[ 4  6  5]
 [ 7 23 48]
 [91 34 85]]"""
print("---------------------------")

# arr=np.array([3,76,52,86,45,5,13,7,34])
idx=np.argsort(arr)
print(idx)      # [0 5 7 6 8 4 2 1 3]
print(arr[idx]) # [ 3  5  7 13 34 45 52 76 86]

print("----------------------------")

names=np.array(["John","Jane","Jane","John"])
scores=np.array([95,37,88,59])

index=np.sort((scores,names))
print(index)
"""
[['37' '59' '88' '95']
 ['Jane' 'Jane' 'John' 'John']]"""