import numpy as np

numbers=np.array([1,2,3,4,5,6,7,8,9,10,11,12])
filter_arr=[]
print("--------greater than 7--------")
for item in numbers:
    if item>7:
        filter_arr.append(True)
    else:
        filter_arr.append(False)
new_arr=numbers[filter_arr]
print(filter_arr) # [False, False, False, False, False, False, False, True, True, True, True, True]
print(new_arr) # [ 8  9 10 11 12]
print("--------even numbers--------")
filter2=[]
for item in numbers:
    if item%2==0:
        filter2.append(True)
    else:
        filter2.append(False)
new_arr2=numbers[filter2]

print(filter2) # [False, True, False, True, False, True, False, True, False, True, False, True]
print(new_arr2) # [ 2  4  6  8 10 12]
print("--------without for loops--------")
filter2_1=numbers>7
new_arr3=numbers[filter2_1]

print(filter2_1) # [False False False False False False False  True  True  True  True  True]
print(new_arr3) # [ 8  9 10 11 12]

filter2_2=numbers%2==0
new_arr4=numbers[filter2_2]
print(filter2_2) # [False  True False  True False  True False  True False  True False  True]
print(new_arr4) # [ 2  4  6  8 10 12]
print("--------without filter array--------")

new_arr5=numbers[numbers>7]
print(new_arr5) # [ 8  9 10 11 12]

new_arr6=numbers[numbers%2==0]
print(new_arr6) # [ 2  4  6  8 10 12]
print("--------multiple filtering--------")
new_arr7=numbers[(numbers>7) & (numbers<11)]
print(new_arr7) # [ 8  9 10]

print("--------where function--------")
indx=np.where((numbers>7) & (numbers<11))

print(numbers[indx]) # [ 8  9 10]